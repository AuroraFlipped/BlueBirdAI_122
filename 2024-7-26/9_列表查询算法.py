# 判断name这个人是否在employee此列表中，如果不在，提示，对不此列表查无此人，在就删除
# delindex.根要刚除的索引
employee = ['王保华', '李伟新', '张强', '陈鑫然']
salary = [4000, 5600, 3400, 6000]
name = input("请输入要删除的人名: ")
# 要删除的索引
delindex = None
for i in range(0, len(employee)):
    if employee[i] == name:
        delindex = i
        break
if delindex is not None:
    del employee[delindex]
    del salary[delindex]
    print('成功删除')
else:
    print('对不此列表查无此人')
print(employee, salary)
