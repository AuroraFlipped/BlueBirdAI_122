import csv

filepath = r'D:\ST\Code\BluAIPycharmProject\examination\第二次测试\通讯录.text'
employees = []
salarys = []
while True:
    menu = input('1.添加联系人2.查找联系人3.删除联系人4.修改联系人输入0退出')
    if menu == '0':
        break
    if menu == '1':
        name = input('请输入姓名：')
        salary = input('请输入薪资：')
        employees.append(name)
        salarys.append(salary)
        print('添加成功')
    if menu == '2':
        for e, s in zip(employees, salarys):
            print(e, s)
    if menu == '3':
        delindex = None
        name = input('请输入你要删除人的姓名')
        for i in range(len(employees)):
            if employees[i] == name:
                delindex = i
                break
            if delindex is not None:
                del employees[delindex]
                del salarys[delindex]
                print('删除成功')
            else:
                print('查无此人')
    if menu == '4':
        updateindex = None
        name = input('请输入修改人姓名：')
        for i in range(len(employees)):
            if employees[i] == name:
                updateindex = i
                break
            if updateindex is not None:
                salary = input('请输入要修改的工资')
                salarys[updateindex] = salary
                print('修改成功')
            else:
                print('查无此人')
with open(filepath, mode='w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([name, salary])