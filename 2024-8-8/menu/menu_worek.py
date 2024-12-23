names = []
tels = []


def adduser(name, tel):
    names.append(name)
    tels.append(tel)
    print('添加成功')


def checkuser():
    print('-' * 10, '通讯录', '-' * 10)
    print(f'姓名\t\t\t电话')
    for i in range(len(names)):
        print(f'{names[i]}\t\t{tels[i]}')
    print('-' * 29)


def updateuser(name):
    flag = None
    for i in range(len(names)):
        if names[i] == name:
            flag = i
            break
    if flag is not None:
        tel = input('请输入要修改的电话：')
        tels[flag] = tel
        print('修改成功')
    else:
        print('查无此人')


def deleuser(name):
    flag = None
    for i in range(len(names)):
        if names[i] == name:
            flag = i
            break
    if flag is not None:
        del names[flag]
        del tels[flag]
        print('删除成功')
    else:
        print('查无此人')
