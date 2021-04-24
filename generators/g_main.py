from jinja2 import Environment, FileSystemLoader

songs = ["s_0", "s_1"]
notes = ["n_C5"]

file_loader = FileSystemLoader('generators/templates')
env = Environment(loader=file_loader)
#env.lstrip_blocks = True
#env.rstrip_blocks = True
#env.trim_blocks = True

template = env.get_template('main.py.jinja')

template.stream(notes=notes, songs=songs).dump('main.py')
# output = template.render(notes = notes)
# print(output)
