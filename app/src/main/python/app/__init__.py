"""TITAN PRO GOV. Everything the program writes (data, memory, logs, settings, keys, bytecode) lives ONLY in ZZZ/."""
import os as _os
import sys as _sys

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_DATA = _os.path.expanduser(_os.getenv("TITAN_DATA", _os.path.join(_HERE, "ZZZ")))
_sys.pycache_prefix = _os.path.join(_DATA, "pycache")
