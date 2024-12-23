# 父类Car
class Car():
    def __init__(self, speed='50km'):
        self.speed = speed

    def show(self):
        print('这辆车的速度：', self.speed)


# 子类继承父类
class HomeCar(Car):
    pass


bus = HomeCar()
bus.show()
# 子类依然可以定义父类参数
bus1 = HomeCar('60km')
bus1.show()
