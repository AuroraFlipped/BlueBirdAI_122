employees = []
salarys = []


def add_tongxun(name, salary):
    employees.append(name)
    salarys.append(salary)
    print('添加成功')


def check_tongxun():
    for e, s in zip(employees, salarys):
        print(e, s)


def delete_tongxun(name):
    flag = None
    for i in range(len(employees)):
        if employees[i] == name:
            flag = i
            break
        if flag is not None:
            del employees[flag]
            del salarys[flag]
            print('删除成功')
        else:
            print('查无此人')


def update_tongxun(name):
    flag = None
    for i in range(len(employees)):
        if employees[i] == name:
            flag = i
            break
        if flag is not None:
            salay = input('请输入修改工资：')
            salarys[flag] = salay
            print('修改成功')
        else:
            print('查无此人')
