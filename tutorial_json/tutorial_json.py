import json


json_string = '''
    {
        "studensts" : [
            {
                "id" : 1,
                "name" : "Tim",
                "age" : 21,
                "full-time" : true
            },
            {
                "id" : 2,
                "name" : "Joe",
                "age" : 33,
                "full-time" : false               
            }
        ]
    }
'''

data = json.loads(json_string)

print(data["studensts"])
# [{'id': 1, 'name': 'Tim', 'age': 21, 'full-time': True}, {'id': 2, 'name': 'Joe', 'age': 33, 'full-time': False}]

print(data["studensts"][0])
# {'id': 1, 'name': 'Tim', 'age': 21, 'full-time': True}

print(*data["studensts"][0])
# id name age full-time

print(data["studensts"][0]['id'])
# 1


data = json.loads(json_string)
data['test'] = True

print(data)
# {'studensts': [...], 'test': True}

new_json = json.dumps(data, indent= 2)
print(new_json)
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
  ],
  "test": true
}
'''

new_json = json.dumps(data, indent= 2, sort_keys=True)
print(new_json)
'''
{
  "studensts": [
    {
      "age": 21,
      "full-time": true,
      "id": 1,
      "name": "Tim"
    },
    {
      "age": 33,
      "full-time": false,
      "id": 2,
      "name": "Joe"
    }
  ],
  "test": true
}
'''