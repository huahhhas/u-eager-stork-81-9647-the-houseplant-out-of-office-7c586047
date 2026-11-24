#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to $OUTPUT_DIR/entry.txt (default /output), with no trailing newline,
then self-verifies the written file.
Standard library only.
"""

import os
import sys

LINE = "Out of office: I'm the fern you forgot in March. I've never been happier. Your email can wait. So can I."

MAX_CHARS = 120


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: UTF-8, 1-120 chars, exact match, no trailing newline.
    with open(path, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")  # raises if not valid UTF-8
    assert written == data, "written bytes differ from the line"
    assert text == LINE, "written text differs from the line"
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1-{MAX_CHARS}"
    assert text.strip(), "line must not be only whitespace"
    assert not written.endswith(b"\n"), "entry must have no trailing newline"

    print(f"wrote {path} ({len(text)} chars, {len(written)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
