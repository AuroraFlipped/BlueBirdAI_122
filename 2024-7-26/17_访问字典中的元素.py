info = {
    'name': '张三',
    'age': '18',
    'email': 'zhangsan@163.com',
}
# 方法一：
print(info['age'])
# 方法二：
print(info.get('age'))
print(info.get('sex'))
# 你猜为指定返回值当为空时就会返回设定的
print(info.get('sex', '你猜'))
# 字典当中可以有列表
employee_info = {'emp1': ['王保华', 4000], 'emp2': ['李伟新', 5600], 'emp3': ['张强', 3400], 'emp4': ['陈鑫然', 6000]}
# 列表当中可以有字典
list1 = [{'username': 'msh', 'age': '47'}, {'username': 'msh', 'age': '47'}]
