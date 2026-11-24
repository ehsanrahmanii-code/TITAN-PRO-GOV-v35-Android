#!/usr/bin/env python3
"""TITAN PRO Clean — entry point. Everything the app writes (data, memory, logs, bytecode cache) lives only in ZZZ/."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_DATA = os.path.expanduser(os.getenv("TITAN_DATA", os.path.join(_HERE, "ZZZ")))
sys.pycache_prefix = os.path.join(_DATA, "pycache")      # no __pycache__ folders next to the code

from app.web.app import main  # noqa: E402

if __name__ == "__main__":
    main()
