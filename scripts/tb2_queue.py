#!/usr/bin/env python3
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from tb2_claude_bench.queue import main

if __name__ == "__main__":
    raise SystemExit(main())
