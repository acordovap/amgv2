from jinja2 import Environment, FileSystemLoader
from grammar import validator
import json

file_loader = FileSystemLoader('generators/templates')
env = Environment(loader=file_loader)

with open("grammar/example.json", "r") as read_file:
    jdata = json.load(read_file)

v = validator.validateJson(jdata)
if v:
    for s in jdata:
        t_list = []
        for t in s["s_tracks"]:
            t_list.append(t["t_name"])
        template = env.get_template('song.py.jinja')
        template.stream(tracks=t_list).dump('agents/'+s["s_name"]+'.py')

else:
    print("Given JSON data is InValid")
    print(jdata)
