import sys
from pathlib import Path
from typing import Any

import tomllib


def loadv(argv: list[str]) -> dict[str, Any]:
    try:
        if any(arg in ["-h", "--help"] for arg in argv):
            sys.stderr.write(f"Usage: python3 -m {Path(argv[0]).parent.name} TOML\n")
            sys.exit(0)
        with Path.open(sys.argv[1], "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
