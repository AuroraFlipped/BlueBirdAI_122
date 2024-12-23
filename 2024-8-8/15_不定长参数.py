# 一个*号代表元组（tuple）
def func1(name, *num):
    print(f'{name}数字为{num}')


func1('张三', 4, 5, 6)


# 两个*号代表字典（dict）
def func2(name, **num):
    # print(f'{name}信息为{num}')
    print(f'{name}')
    for k, v in num.items():
        print(k, v)


func2('李四', addr='火星', email='dong163@.com', )
