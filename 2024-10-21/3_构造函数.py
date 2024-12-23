class Person():
    # 下面叫构造方法，也叫初始化方法，当对象被创建时直接调用
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def say(self):
        print(f'我叫{self.name},今年{self.age}岁')


p1 = Person('张三', 14)
p1.say()

p2 = Person('李四', 18)
p2.say()
