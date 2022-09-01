# JavaScript Object Notation

import json

with open("tutorial_json\data.json", "r") as f:
    data = json.load(f)



print(json.dumps(data, indent=4))
'''
{
    "studensts": [
        {
            "id": 1,
            "name": "Tim",
            "age": 21,
            "full-time": true
        },
        {
            "id": 2,
            "name": "Joe",
            "age": 33,
            "full-time": false
        }
    ]
}
'''

print(data.items())
#  dict_items([('studensts', [{'id': 1, 'name': 'Tim', 'age': 21, 'full-time': True}, {'id': 2, 'name': 'Joe', 'age': 33, 'full-time': False}])])
















