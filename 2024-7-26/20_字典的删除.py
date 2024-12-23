info = {
    'name': '张三',
    'age': '18',
    'email': 'zhangsan@163.com',
}
print(info)
# 第一种del
del info['age']
print(info)
# 第二种pop
info.pop('email')
print(info)
# 第三种clear
info.clear()
print(info)
