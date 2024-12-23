'''
针对刚才的员工工资信息，我们完成如下需求：

- 程曦入职，工资7900
- 陈鑫然离职，删除其信息
- 王保华涨工资为6000
'''
employee = ['王保华', '李伟新', '张强', '陈鑫然']
salary = [4000, 5600, 3400, 6000]
# 原来状态
print(employee, salary)
# 程曦入职
employee.append('程曦')
salary.append(7900)
print(employee, salary)
# 陈鑫然离职
del employee[3]
del salary[3]
print(employee, salary)
# 王保华涨工资
salary[0] = 6000
print(employee, salary)
