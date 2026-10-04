#!/usr/bin/env python3
"""Local before/after server for the Aizomea manuscript preview.

The preview compares the main branch (by default) with the editable
working-tree prologue and files in ../2-entries/. The branch is resolved on
every poll, so committing on main makes the panes converge without restarting
the server; committing on an editorial branch leaves the comparison against
main intact.

GET /api/files             -> current canonical manuscript filenames
GET /api/meta              -> baseline and path information
GET /api/reviews           -> manuscript files reviewed at their current content
GET /api/original/<file>   -> file content at the fixed Git baseline
GET /api/current/<file>    -> working-tree file content
PUT /api/current/<file>    -> atomically updates the working-tree file
PUT /api/review/<file>     -> marks or unmarks the current content as reviewed

Run: python3 preview-server.py [port] [base-ref]
     default port: 8765
     default base-ref: main
"""

import hashlib
import http.server
import json
import os
import stat
import subprocess
import sys
import tempfile
import threading
import urllib.parse


WORKBENCH_DIR = os.path.dirname(os.path.abspath(__file__))
STORY_DIR = os.path.dirname(WORKBENCH_DIR)
ENTRIES_DIR = os.path.join(STORY_DIR, "2-entries")
PROLOGUE_NAME = "1-prologue.md"
PROLOGUE_PATH = os.path.join(STORY_DIR, PROLOGUE_NAME)
REVIEW_STATE_FILE = os.path.join(WORKBENCH_DIR, ".preview-reviews.json")
BASE_REF = sys.argv[2] if len(sys.argv) > 2 else "main"
REVIEW_LOCK = threading.Lock()


def git(*args):
    return subprocess.run(
        ["git", "-C", STORY_DIR, *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


BASE_COMMIT = None
BASELINE_CACHE = {}


def baseline_commit():
    """Resolve the comparison branch and invalidate stale cached originals."""
    global BASE_COMMIT  # noqa: PLW0603
    resolved = git("rev-parse", "--verify", f"{BASE_REF}^{{commit}}")
    if resolved.returncode:
        message = resolved.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"Cannot resolve Git baseline {BASE_REF!r}: {message}")
    commit = resolved.stdout.decode("ascii").strip()
    if commit != BASE_COMMIT:
        BASE_COMMIT = commit
        BASELINE_CACHE.clear()
    return commit


try:
    baseline_commit()
except RuntimeError as exc:
    raise SystemExit(str(exc)) from exc


def manuscript_names():
    """Return the prologue followed by canonical entries in numeric order."""
    try:
        names = os.listdir(ENTRIES_DIR)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Entry directory is missing: {ENTRIES_DIR}") from exc
    entries = sorted(
        name
        for name in names
        if name.endswith(".md") and os.path.isfile(os.path.join(ENTRIES_DIR, name))
    )
    if not os.path.isfile(PROLOGUE_PATH):
        raise RuntimeError(f"Prologue is missing: {PROLOGUE_PATH}")
    return [PROLOGUE_NAME, *entries]


def manuscript_path(name):
    """Return the working-tree path for one validated manuscript filename."""
    if name == PROLOGUE_NAME:
        return PROLOGUE_PATH
    return os.path.join(ENTRIES_DIR, name)


def git_path(name):
    """Return the repository-relative path for one manuscript filename."""
    if name == PROLOGUE_NAME:
        return PROLOGUE_NAME
    return f"2-entries/{name}"


def validated_name(raw):
    """Resolve one URL filename without permitting traversal or new files."""
    name = urllib.parse.unquote(raw)
    if not name or name != os.path.basename(name) or not name.endswith(".md"):
        return None
    if name not in set(manuscript_names()):
        return None
    return name


def baseline_bytes(name):
    """Load a file from the latest commit on the comparison branch."""
    commit = baseline_commit()
    if name not in BASELINE_CACHE:
        result = git("show", f"{commit}:{git_path(name)}")
        BASELINE_CACHE[name] = result.stdout if result.returncode == 0 else None
    return BASELINE_CACHE[name]


def content_digest(name):
    """Return a stable fingerprint for the current working-tree content."""
    digest = hashlib.sha256()
    with open(manuscript_path(name), "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_review_state():
    """Load and validate the local review ledger without changing it."""
    try:
        with open(REVIEW_STATE_FILE, encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError:
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read review state: {exc}") from exc

    reviewed = value.get("reviewed") if isinstance(value, dict) else None
    if not isinstance(reviewed, dict):
        raise RuntimeError("Review state has an invalid format")
    return {
        name: fingerprint
        for name, fingerprint in reviewed.items()
        if isinstance(name, str) and isinstance(fingerprint, str)
    }


def save_review_state(reviewed):
    """Atomically persist the local review ledger."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=WORKBENCH_DIR,
            prefix=".preview-reviews-",
            delete=False,
        ) as handle:
            temporary = handle.name
            json.dump(
                {"version": 1, "reviewed": reviewed},
                handle,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
        os.replace(temporary, REVIEW_STATE_FILE)
    except Exception:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)
        raise


def reviewed_manuscript_names():
    """Return files whose current bytes match the version that was reviewed."""
    with REVIEW_LOCK:
        reviewed = load_review_state()
        return [
            name
            for name in manuscript_names()
            if reviewed.get(name) == content_digest(name)
        ]


def set_reviewed(name, is_reviewed):
    """Mark the current file version reviewed, or clear its review record."""
    with REVIEW_LOCK:
        reviewed = load_review_state()
        if is_reviewed:
            reviewed[name] = content_digest(name)
        else:
            reviewed.pop(name, None)
        save_review_state(reviewed)


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
            self.send_json(manuscript_names())
            return

        if path == "/api/meta":
            commit = baseline_commit()
            self.send_json(
                {
                    "baseRef": BASE_REF,
                    "baseCommit": commit,
                    "entriesDirectory": ENTRIES_DIR,
                }
            )
            return

        if path == "/api/reviews":
            try:
                self.send_json(reviewed_manuscript_names())
            except (OSError, RuntimeError) as exc:
                self.send_error(500, str(exc))
            return

        for prefix, source in (
            ("/api/original/", "original"),
            ("/api/current/", "current"),
        ):
            if path.startswith(prefix):
                name = validated_name(path[len(prefix) :])
                if name is None:
                    self.send_error(404, "unknown manuscript file")
                    return
                if source == "original":
                    data = baseline_bytes(name)
                    if data is None:
                        self.send_error(404, "manuscript file does not exist at the Git baseline")
                        return
                else:
                    with open(manuscript_path(name), "rb") as handle:
                        data = handle.read()
                self.send_bytes(data, "text/markdown; charset=utf-8")
                return

        super().do_GET()

    def do_PUT(self):
        path = urllib.parse.urlsplit(self.path).path
        review_prefix = "/api/review/"
        if path.startswith(review_prefix):
            name = validated_name(path[len(review_prefix) :])
            if name is None:
                self.send_error(403, "reviews allowed only for canonical manuscript files")
                return

            try:
                length = int(self.headers.get("Content-Length", 0))
                if length > 1024:
                    self.send_error(413, "review request is too large")
                    return
                value = json.loads(self.rfile.read(length).decode("utf-8"))
                is_reviewed = value.get("reviewed") if isinstance(value, dict) else None
                if not isinstance(is_reviewed, bool):
                    self.send_error(400, "expected a boolean 'reviewed' value")
                    return
                set_reviewed(name, is_reviewed)
            except (OSError, UnicodeDecodeError, json.JSONDecodeError, RuntimeError) as exc:
                self.send_error(500, str(exc))
                return

            self.send_json({"name": name, "reviewed": is_reviewed})
            return

        prefix = "/api/current/"
        if not path.startswith(prefix):
            self.send_error(403, "writes allowed only through /api/current/<file>.md")
            return

        name = validated_name(path[len(prefix) :])
        if name is None:
            self.send_error(403, "writes allowed only to existing canonical manuscript files")
            return

        temporary = None
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            destination = manuscript_path(name)
            destination_mode = stat.S_IMODE(os.stat(destination).st_mode)
            with tempfile.NamedTemporaryFile(
                dir=os.path.dirname(destination), prefix=".preview-", delete=False
            ) as handle:
                temporary = handle.name
                handle.write(data)
                os.fchmod(handle.fileno(), destination_mode)
            os.replace(temporary, destination)
            try:
                # Saving after any edit starts a fresh review cycle, even if
                # the final bytes happen to match the previously reviewed text.
                set_reviewed(name, False)
            except (OSError, RuntimeError) as exc:
                # The manuscript save has already succeeded. Do not misreport
                # it as failed just because the separate local ledger is bad.
                super().log_message("could not clear review state: %s", exc)
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
    print(f"before: live {BASE_REF} ({baseline_commit()[:10]})")
    print(f"edited: {PROLOGUE_PATH} + {ENTRIES_DIR}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
