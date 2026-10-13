#!/usr/bin/env python3
"""Create a safe aggregate inventory without exposing local filenames."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def build_inventory(root: Path) -> dict[str, object]:
    if not root.is_dir():
        raise SystemExit(f"Source directory does not exist: {root}")
    extensions: Counter[str] = Counter()
    total_bytes = 0
    file_count = 0
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        file_count += 1
        total_bytes += path.stat().st_size
        extensions[path.suffix.lower() or "[no extension]"] += 1
    return {
        "file_count": file_count,
        "total_bytes": total_bytes,
        "extensions": dict(sorted(extensions.items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    print(json.dumps(build_inventory(args.root), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
