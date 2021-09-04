import json

with open('colors.json', 'r') as f:
    data = json.load(f)

print(data['Standart'])