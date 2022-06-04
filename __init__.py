import sys
import os
import re
import json
from cuda_fmt import get_config_filename

PY_OK = sys.version_info[:2] >= (3, 6)
if PY_OK:
    sys.path.insert(0, os.path.dirname(__file__))
    from . import black
    from .black import TargetVersion as Ver

    ver35 = {
            Ver.PY35,
            Ver.PY36,
            Ver.PY37,
            Ver.PY38,
            Ver.PY39,
            Ver.PY310,
            }
    ver36 = {
            Ver.PY36,
            Ver.PY37,
            Ver.PY38,
            Ver.PY39,
            Ver.PY310,
            }
    ver37 = {
            Ver.PY37,
            Ver.PY38,
            Ver.PY39,
            Ver.PY310,
            }
    ver38 = {
            Ver.PY38,
            Ver.PY39,
            Ver.PY310,
            }
    ver39 = {
            Ver.PY39,
            Ver.PY310,
            }
    ver310 = {
            Ver.PY310,
            }

    ver_map = {
        'py35': ver35,
        'py36': ver36,
        'py37': ver37,
        'py38': ver38,
        'py39': ver39,
        'py310': ver310,
    }


def get_mode():

    fn = get_config_filename('Python Black')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    d = json.loads(s)

    line_len = d.get('line_len', black.DEFAULT_LINE_LENGTH)
    norm = d.get('string_normalization', True)
    target = d.get('target')

    return black.FileMode(
        target_versions = ver_map.get(target, ver36),
        line_length = line_len,
        string_normalization = norm
        )


def do_format(text):

    if not PY_OK:
        return
    mode = get_mode()
    #print(mode)
    text = black.format_str(text, mode=mode)
    return text
