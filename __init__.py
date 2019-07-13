import sys
import os
import re
import json
from cuda_fmt import get_config_filename

PY_OK = sys.version_info[:2] >= (3, 6)
if PY_OK:
    sys.path.append(os.path.dirname(__file__))
    from . import black


def get_mode():

    fn = get_config_filename('Python Black')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    d = json.loads(s)

    line_len = d.get('line_len', black.DEFAULT_LINE_LENGTH)
    norm = d.get('string_normalization', True)
    v = d.get('target')

    if v=='py27':
        ver = {
            black.TargetVersion.PY27,
            black.TargetVersion.PY33,
            black.TargetVersion.PY34,
            black.TargetVersion.PY35,
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    elif v=='py33':
        ver = {
            black.TargetVersion.PY33,
            black.TargetVersion.PY34,
            black.TargetVersion.PY35,
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    elif v=='py34':
        ver = {
            black.TargetVersion.PY34,
            black.TargetVersion.PY35,
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    elif v=='py35':
        ver = {
            black.TargetVersion.PY35,
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    elif v=='py36':
        ver = {
            black.TargetVersion.PY36,
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    elif v=='py37':
        ver = {
            black.TargetVersion.PY37,
            black.TargetVersion.PY38,
            }
    else:
        ver = {
            black.TargetVersion.PY38,
            }

    return black.FileMode(
        target_versions=ver, 
        line_length=line_len,
        string_normalization=norm
        )


def do_format(text):

    if not PY_OK:
        return
    mode = get_mode()
    #print(mode)
    text = black.format_str(text, mode=mode)
    return text
