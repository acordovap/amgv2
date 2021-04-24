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

# # Convert json to python object.
# example =[
#     {
#         "s_name": "s1",
#         "s_tempo": 120,
#         "s_key_signature": "C",
#         "s_time_signature": [2,3],
#         "s_progressions": ["I", "II"],
#         "s_tracks": [
#             {
#                 "t_name": "t1",
#                 "t_notes": [
#                     {
#                         "n_name": "C-5",
#                         "n_behavs": [
#                             {
#                                 "b_name": "b1",
#                                 "b_cmd": "cmd1"
#                             },
#                             {
#                                 "b_name": "b2",
#                                 "b_cmd": "cmd1"
#                             }
#                         ]
#                     },
#                     {
#                         "n_name": "C-6",
#                         "n_behavs": [
#                             {
#                                 "b_name": "b1",
#                                 "b_cmd": "cmd1"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "t_name": "t2",
#                 "t_notes": [
#                     {
#                         "n_name": "C-5",
#                         "n_behavs": [
#                             {
#                                 "b_name": "b1",
#                                 "b_cmd": "cmd1"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ]
#     },
#     {
#         "s_name": "s2",
#         "s_tempo": 120,
#         "s_key_signature": "f#",
#         "s_time_signature": [1,2],
#         "s_progressions": ["I"],
#         "s_tracks": [
#             {
#                 "t_name": "t1",
#                 "t_notes": [
#                     {
#                         "n_name": "C-5",
#                         "n_behavs": [
#                             {
#                                 "b_name": "b1",
#                                 "b_cmd": "cmd1"
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ]
#     }
# ]
#
# jsonData = json.loads(json.dumps(example))
# # validate it
# isValid = validateJson(jsonData)
# if isValid:
#     print(jsonData)
#     print("Given JSON data is Valid")
# else:
#     print(jsonData)
#     print("Given JSON data is InValid")
