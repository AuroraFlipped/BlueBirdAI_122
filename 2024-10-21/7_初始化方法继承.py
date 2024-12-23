class Base():
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
        print('继承了Base这个类')
        print('我的名字',self.name)
        print('我的年龄',self.age)
        print('我的学号',self.id)

    def goTo_shool(self):
        print(f'{self.name}正在使用Base类中的goTo_shool方法去上学')

# 继承父类的时候会继承父类中所有方法
class Student(Base):
    pass

xiaohong = Student('小红',18,1001)
xiaohong .goTo_shool()