# 类名使用大驼峰表示：GoodStudy，DayDayUpUp
# 属性及方法使用小驼峰表示：goodStudy
class Person():
    # 添加属性
    name = ''
    age = 0

    # 构造方法 self当前对象 其他语法用this
    def say(self):
        print('我爱说话')

    def walk(self):
        print('我会走路')


# 创建一个对象p1
p1 = Person()
p1.name = '张三'
p1.age = 18
print(p1.name)
print(p1.age)
p1.say()
p1.walk()

# 创建另一个对象p2
p2 = Person()
p2.name = '李四'
p2.age = 20
print(p2.name)
print(p2.age)
p2.say()
p2.walk()
