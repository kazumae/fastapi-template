#!/usr/bin/env python

import subprocess
from pathlib import Path


def run_command(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    src_dir = Path("src")

    # isort
    run_command(["isort", str(src_dir)])

    # black
    run_command(["black", str(src_dir)])

    # flake8
    run_command(["flake8", str(src_dir)])

    # mypy
    run_command(["mypy", str(src_dir)])


if __name__ == "__main__":
    main()
