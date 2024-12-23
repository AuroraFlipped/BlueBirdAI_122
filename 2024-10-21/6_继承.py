class HuoYuanJia():
    def huoJiaQuan(self):
        print('霍家拳')

    def huoJiaTui(self):
        print('霍家腿')


class HuoDongGe(HuoYuanJia):
    pass


h1 = HuoDongGe()
h1.huoJiaTui()
h1.huoJiaQuan()
