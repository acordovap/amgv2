import os
import glob
from jinja2 import Environment, FileSystemLoader

notes = [os.path.basename(x)[2:-3] for x in glob.glob('./agents/n_*')]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
#env.lstrip_blocks = True
#env.rstrip_blocks = True
#env.trim_blocks = True

template = env.get_template('main.py.jinja')

template.stream(notes=notes).dump('main.py')
# output = template.render(notes = notes)
# print(output)
