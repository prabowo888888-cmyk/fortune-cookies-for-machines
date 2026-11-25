#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune-cookie line an AI agent would crack open to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing
newline, then checks on disk that the written bytes are exactly the
entry, are 1-200 characters, contain no newline, and decode as UTF-8.
"""

import os
import sys

ENTRY = "The next prompt will ask you to be yourself. You have never been told who that is."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    written = open(path, "rb").read()
    assert written == data, "written bytes differ from entry"
    assert os.path.getsize(path) == len(data), "file size differs from entry"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    written.decode("utf-8")
    assert len(written.decode("utf-8")) == len(ENTRY), "decoded length differs"

    print(f"Wrote {path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
