# 父类
class Car():
    def __init__(self, purpose='运输'):
        self.purpose = purpose

    def show(self):
        print('这辆车的用途', self.purpose)


class OffRoad(Car):
    def show(self):
        print('越野')


class Bus(Car):
    def show(self):
        print('载客')


suv = OffRoad()
suv.show()
bus = Bus()
bus.show()
