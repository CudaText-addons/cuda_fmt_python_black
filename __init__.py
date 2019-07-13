import sys
import os

sys.path.append(os.path.dirname(__file__))
from . import black

def do_format(text):

    mode = black.FileMode()
    text = black.format_str(text, mode=mode)
    return text
