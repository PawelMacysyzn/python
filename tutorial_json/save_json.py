import json


with open('tutorial_json\data.json', 'r') as f:
    data = json.load(f)


with open('tutorial_json\data_2.json', 'w') as f:
    json.dump(data, f)

with open('tutorial_json\data_sort.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)