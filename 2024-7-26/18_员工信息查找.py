employee_info = {'emp1': ['王保华', 4000], 'emp2': ['李伟新', 5600], 'emp3': [' 张强', 3400], 'emp4': ['陈鑫然', 6000]}
# 第一种方法
emp_num = 'emp2'
if emp_num in employee_info:
    employee2 = employee_info[emp_num]
    print('工号为', emp_num, '的员工信息如下：')
    print(employee_info[emp_num])
else:
    print('工号不存在')
# 第二种方法
emp_num = 'emp5'
employee2 = employee_info.get(emp_num)
if employee2 is not None:
    print('工号为', emp_num, '的员工信息如下：')
    print(employee_info[emp_num])
else:
    print('工号不存在')
