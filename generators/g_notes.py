from jinja2 import Environment, FileSystemLoader

songs = ["s_0", "s_1"]
notes = ["n_C5"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
#env.lstrip_blocks = True
#env.rstrip_blocks = True
#env.trim_blocks = True

template = env.get_template('note.py.jinja')

for note in notes:
    template.stream(songs=songs, note=note).dump('agents/'+note+'.py')
