import json 

with open("students.json", "r") as file:
    data = file.read()

parsed = json.loads(data)

print(parsed["name"])