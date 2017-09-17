import os
from pathlib import Path
import codecs

def get_template(name: str, decode='utf-8') -> str:
    current_path = Path(os.path.abspath(__file__)).parent
    template_path = current_path.parent.joinpath('_templates')
    template_file = template_path.joinpath(name).as_posix()
    with codecs.open(template_file, 'r','utf-8') as fp:
        return fp.read()
