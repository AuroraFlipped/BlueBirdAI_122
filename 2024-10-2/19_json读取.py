import json

filepath = r'/2024-10.2\data\student.text'
with open(filepath, 'r', encoding='utf-8') as f:
    stu = json.load(f)
print(stu['name'])
print(stu['tel'])
print(stu['parents'])
print(stu['parents'][1])
