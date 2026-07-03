#!/usr/bin/env python3
"""Tiny writable static server for the Aizomea before/after preview.

GET  -> serves files from this directory (same as http.server).
PUT  -> writes the request body to a path, but ONLY under entries-v2/.

Run:  python3 preview-server.py [port]   (default 8765)
"""
import http.server
import os
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
WRITABLE = os.path.join(ROOT, "entries-v2")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        rel = urllib.parse.unquote(self.path.lstrip("/"))
        full = os.path.abspath(os.path.join(ROOT, rel))
        # Confine writes to entries-v2/ and reject anything that escapes it.
        if not full.startswith(WRITABLE + os.sep) or not full.endswith(".md"):
            self.send_error(403, "writes allowed only under entries-v2/*.md")
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            with open(full, "wb") as f:
                f.write(data)
        except Exception as e:  # noqa: BLE001
            self.send_error(500, str(e))
            return
        self.send_response(204)
        self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):  # quieter console
        if self.command == "PUT":
            super().log_message(fmt, *args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    os.chdir(ROOT)
    httpd = http.server.HTTPServer(("127.0.0.1", port), Handler)
    print(f"preview server on http://localhost:{port}/preview.html  (writes -> entries-v2/)")
    httpd.serve_forever()
