import os
from pathlib import Path

def get_template(name: str, decode='utf-8') -> str:
    current_path = Path(os.path.abspath(__file__)).parent
    template_path = current_path.parent.joinpath('_templates')
    template_file = template_path.joinpath(name).as_posix()
    with open(template_file, 'r') as fp:
        return fp.read()
