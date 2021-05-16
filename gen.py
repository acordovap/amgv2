from jinja2 import Environment, FileSystemLoader
from grammar import validator
from grammar import amglang
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

with open("grammar/example3.json", "r") as read_file:
    jdata = json.load(read_file)

v = validator.validateJson(jdata)
if v:
    for s in jdata:
        t_list = []
        for t in s["s_tracks"]:
            t_list.append(t["t_name"])
            n_list = []
            for n in t["t_notes"]:
                n_list.append(n["n_name"])
                b_list = []
                for b in n["n_behavs"]:
                    # maybe first test all behaviors, not here
                    newcmd = amglang.compile(b["b_cmd"])
                    b["b_cmd"] = newcmd
                    b_list.append(b)
                # Generate notes agents
                template = env.get_template('note.py.jinja')
                template.stream(song=s["s_name"], track=t["t_name"], note=n["n_name"], behavs=b_list).dump('agents/'+s["s_name"]+'_'+t["t_name"]+'_'+n["n_name"].replace('-', '')+'.py')
        # Generate songs agents
        template = env.get_template('song.py.jinja')
        template.stream(song=s).dump('agents/'+s["s_name"]+'.py')
    # Generate setup
    template = env.get_template('setup.py.jinja')
    template.stream(songs=jdata).dump('setup.py')
    # Generate main
    template = env.get_template('main.py.jinja')
    template.stream(songs=jdata).dump('main.py')

else:
    print("Given JSON data is InValid")
    print(jdata)
