employee = ['张三', '李四', '王五', '赵六']
salary = [4000, 5600, 3400, 6000]
ages = [16, 13, 15, 16]
for e, s, a in zip(employee, salary, ages):
    print(f'姓名{e},薪资{s},年龄{a}')
