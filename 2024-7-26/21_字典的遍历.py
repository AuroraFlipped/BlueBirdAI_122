info = {
    'name': '张三',
    'age': '18',
    'email': 'zhangsan@163.com',
}
# 访问
print(info['username'])
# 方法1
for key in info:
    print(key, info[key])
# 方法2
for key, value in info.items():
    print(key, value)
