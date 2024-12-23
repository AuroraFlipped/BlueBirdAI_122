# 需求：利用面向对象的继承方面知识，完成动物年龄的输出。
# 具体要求：
# 设计父类Animal,实现方法print_info(),打印年龄信息
# 设计子类Bird、Fish,重写print_info()
class Animal():
    name = ''
    age = ''
    def __init__(self, n,a):
        self.name = n
        self.age = a
    def print_info(self):
        print(self.name,'年龄',self.age)

class Bird(Animal):
    def print_info(self):
        super().print_info()
        print('唱歌')


class Fish(Animal):
    def print_info(self):
        super().print_info()
        print('游泳')

b = Bird('麻雀',5)
b.print_info()
f = Fish('金鱼',3)
f.print_info()