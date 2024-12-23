employee = ['王保华', '李伟新', '张强', '陈鑫然']
salary = [4000, 5600, 3400, 6000]
name = input('请输入你要修改的姓名：')
# 放到这里即便查无此人也还要输入sal
# sal = int(input('请输入你要修改的工资：'))
updateindex = None
for i in range(0, len(employee)):
    if employee[i] == name:
        updateindex = i
        break
if updateindex is not None:
    sal = int(input('请输入你要修改的工资：'))
    salary[updateindex] = sal
    print(employee, salary)
    print('修改成功')
else:
    print('查无此人')
