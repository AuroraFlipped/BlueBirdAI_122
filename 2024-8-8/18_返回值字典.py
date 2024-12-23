# 返回值字典
def intro(name, age, addr):
    result = {'name': name, 'age': age, 'addr': addr}
    return result


n = input('输入用户名：')
a = input('输入年龄：')
r = input('输入地址：')
result = intro(age=a, addr=r, name=n)
print(result)
