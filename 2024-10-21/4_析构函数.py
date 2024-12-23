class Person():
    # 下面叫构造方法，也叫初始化方法，当对象被创建时直接调用
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def say(self):
        print(f'我叫{self.name},今年{self.age}岁')

    # 下面为析构函数，当对象被销毁时就触发
    def __del__(self):
        print(f'别删除{self.name}')


p1 = Person('张三', 14)
p1.say()

p2 = Person('李四', 18)
p2.say()
# 当对象被销毁就执行，这个对象是指所有的对象，同时那个被先调用就先从哪个对象开始执行析构函数
del p2
