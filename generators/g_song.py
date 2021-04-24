from jinja2 import Environment, FileSystemLoader

tracks = ["t1", "t2"]

file_loader = FileSystemLoader('generators/templates')
env = Environment(loader=file_loader)
#env.lstrip_blocks = True
#env.rstrip_blocks = True
#env.trim_blocks = True

template = env.get_template('song.py.jinja')

template.stream(tracks=tracks).dump('agents/song.py')
#output = template.render(tracks = tracks)
#print(output)
