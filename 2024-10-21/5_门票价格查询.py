class SelectPrice():
    name = ''
    age = ''

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def showPrice(self):
        if self.age >= 18 and self.age <= 60:
            print(f'姓名为{self.name}，年龄为{self.age}，门票去全价')
        elif self.age >= 60 and self.age <= 6:
            print(f'姓名为{self.name}，年龄为{self.age}，门票去免费')
        else:
            print(f'姓名为{self.name}，年龄为{self.age}，门票去半价')


name = input('enter your name: ')
age = input('enter your age: ')
if age.isdigit() == False:
    print('年龄输入有误')
else:
    s1 = SelectPrice(name, int(age))
    s1.showPrice()
