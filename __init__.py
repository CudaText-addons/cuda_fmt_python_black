import sys
import os

PY_OK = sys.version_info[:2] >= (3, 6)
if PY_OK:
    sys.path.append(os.path.dirname(__file__))
    from . import black

def do_format(text):

    if not PY_OK: return
    mode = black.FileMode()
    text = black.format_str(text, mode=mode)
    return text
