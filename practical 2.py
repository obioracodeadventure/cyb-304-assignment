import pandas as pd
import json



data = pd.read_csv("students.csv")

print(data.head())
print(data.info())

# Real-world use:
# Bank transaction reports, audit records

# 2. JSON Parsing

json_string = '{"name": "Ayo", "age": 22}'

parsed = json.loads(json_string)

print(parsed["name"])  # Output: Ayo

# Real-world use:
# Social media APIs, cloud configs