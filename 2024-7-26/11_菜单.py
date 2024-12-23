employees = []
salarys = []
while True:
    menu = input('请输入1.员工入职2.员工离职3.员工调薪4.查看信息0退出')
    if menu == '0':
        break
    elif menu == '1':
        print('员工入职')
        name = input('输入姓名')
        salary = input('请输入薪资')
        employees.append(name)
        salarys.append(salary)
    elif menu == '2':
        print('员工离职')
        name = input('请输入员工姓名')
        delindex = None
        for i in range(0, len(employees)):
            if employees[i] == name:
                delindex = i
                break
        if delindex is not None:
            del employees[delindex]
            del salarys[delindex]
            print('成功离职')
        else:
            print('查无此人')
    elif menu == '3':
        print('员工调薪')
        name = input('请输入员工姓名')
        updateindex = None
        for j in range(0, len(employees)):
            if employees[j] == name:
                updateindex = j
                break
        if updateindex is not None:
            sal = int(input('请输入调薪之后的薪资'))
            salarys[updateindex] = sal
        print(f'成功为{name}办理调薪成功')
    elif menu == '4':
        print('查看信息')
        for e, s in zip(employees, salarys):
            print(f'员工姓名{e}\t\t薪资为{s}')
