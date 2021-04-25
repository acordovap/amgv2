import json
import jsonschema
from jsonschema import validate

with open("grammar/schema.json", "r") as read_file:
    amgSchema = json.load(read_file)

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=amgSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
