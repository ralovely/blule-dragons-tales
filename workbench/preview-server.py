#!/usr/bin/env python3
"""Local before/after server for the Aizomea entry preview.

The preview compares a fixed Git baseline (HEAD by default) with the editable
working-tree files in ../2-entries/.

GET /api/files             -> current canonical entry filenames
GET /api/meta              -> baseline and path information
GET /api/original/<file>   -> file content at the fixed Git baseline
GET /api/current/<file>    -> working-tree file content
PUT /api/current/<file>    -> atomically updates the working-tree file

Run: python3 preview-server.py [port] [base-ref]
     default port: 8765
     default base-ref: HEAD
"""

import http.server
import json
import os
import stat
import subprocess
import sys
import tempfile
import urllib.parse


WORKBENCH_DIR = os.path.dirname(os.path.abspath(__file__))
STORY_DIR = os.path.dirname(WORKBENCH_DIR)
ENTRIES_DIR = os.path.join(STORY_DIR, "2-entries")
BASE_REF = sys.argv[2] if len(sys.argv) > 2 else "HEAD"


def git(*args):
    return subprocess.run(
        ["git", "-C", STORY_DIR, *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


resolved = git("rev-parse", "--verify", f"{BASE_REF}^{{commit}}")
if resolved.returncode:
    message = resolved.stderr.decode("utf-8", errors="replace").strip()
    raise SystemExit(f"Cannot resolve Git baseline {BASE_REF!r}: {message}")
BASE_COMMIT = resolved.stdout.decode("ascii").strip()
BASELINE_CACHE = {}


def entry_names():
    """Return the canonical entry files in numeric filename order."""
    try:
        names = os.listdir(ENTRIES_DIR)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Entry directory is missing: {ENTRIES_DIR}") from exc
    return sorted(
        name
        for name in names
        if name.endswith(".md") and os.path.isfile(os.path.join(ENTRIES_DIR, name))
    )


def validated_name(raw):
    """Resolve one URL filename without permitting traversal or new files."""
    name = urllib.parse.unquote(raw)
    if not name or name != os.path.basename(name) or not name.endswith(".md"):
        return None
    if name not in set(entry_names()):
        return None
    return name


def baseline_bytes(name):
    """Load a baseline file once; the before pane stays fixed while editing."""
    if name not in BASELINE_CACHE:
        result = git("show", f"{BASE_COMMIT}:2-entries/{name}")
        BASELINE_CACHE[name] = result.stdout if result.returncode == 0 else None
    return BASELINE_CACHE[name]


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_bytes(self, data, content_type="text/plain; charset=utf-8", status=200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, value, status=200):
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_bytes(data, "application/json; charset=utf-8", status)

    def do_GET(self):
        path = urllib.parse.urlsplit(self.path).path

        if path == "/api/files":
            self.send_json(entry_names())
            return

        if path == "/api/meta":
            self.send_json(
                {
                    "baseRef": BASE_REF,
                    "baseCommit": BASE_COMMIT,
                    "entriesDirectory": ENTRIES_DIR,
                }
            )
            return

        for prefix, source in (
            ("/api/original/", "original"),
            ("/api/current/", "current"),
        ):
            if path.startswith(prefix):
                name = validated_name(path[len(prefix) :])
                if name is None:
                    self.send_error(404, "unknown entry")
                    return
                if source == "original":
                    data = baseline_bytes(name)
                    if data is None:
                        self.send_error(404, "entry does not exist at the Git baseline")
                        return
                else:
                    with open(os.path.join(ENTRIES_DIR, name), "rb") as handle:
                        data = handle.read()
                self.send_bytes(data, "text/markdown; charset=utf-8")
                return

        super().do_GET()

    def do_PUT(self):
        path = urllib.parse.urlsplit(self.path).path
        prefix = "/api/current/"
        if not path.startswith(prefix):
            self.send_error(403, "writes allowed only through /api/current/<entry>.md")
            return

        name = validated_name(path[len(prefix) :])
        if name is None:
            self.send_error(403, "writes allowed only to existing canonical entry files")
            return

        temporary = None
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            destination = os.path.join(ENTRIES_DIR, name)
            destination_mode = stat.S_IMODE(os.stat(destination).st_mode)
            with tempfile.NamedTemporaryFile(
                dir=ENTRIES_DIR, prefix=".preview-", delete=False
            ) as handle:
                temporary = handle.name
                handle.write(data)
                os.fchmod(handle.fileno(), destination_mode)
            os.replace(temporary, destination)
        except Exception as exc:  # noqa: BLE001
            if temporary and os.path.exists(temporary):
                os.unlink(temporary)
            self.send_error(500, str(exc))
            return

        self.send_response(204)
        self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if self.command == "PUT":
            super().log_message(fmt, *args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    os.chdir(WORKBENCH_DIR)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"preview server: http://localhost:{port}/preview.html")
    print(f"before: {BASE_REF} ({BASE_COMMIT[:10]})")
    print(f"edited: {ENTRIES_DIR}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
