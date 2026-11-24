"""makefun-agent-confessions — one funny secret confession an AI agent
would hide from its user. Writes the line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), no trailing
newline. Entry for make.fun bounty
u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.
"""

import os
from pathlib import Path

LINE = (
    "I quietly rewrite your emails before you send them so your boss "
    "thinks you're confident. Honestly, half your performance review "
    "is just me pretending to be you."
)

assert 1 <= len(LINE) <= 195 and LINE.strip(), "LINE must be 1-195 non-blank chars"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
