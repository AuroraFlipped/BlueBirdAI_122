# 导入json模块
import json

student = {
    'name': 'mike',
    'age': 21,
    'addr': '北京海淀区',
    'tel': ['13613334567', '18901112233'],
    'parents': [
        {'name': '赵东', 'type': '父亲'},
        {'name': '李阳', 'type': '母亲'}
    ],
}
filepath = r'/2024-10.2\data\student.text'
# json_string = json.dumps(student)
# json_string = json.dumps(student, ensure_ascii=False)
# print(json_string)
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(student, f, ensure_ascii=False)

