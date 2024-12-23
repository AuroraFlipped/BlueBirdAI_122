class HuoYuanJia():
    def huoJiaQuan(self):
        print('霍家拳')

    def huoJiaTui(self):
        print('霍家腿')


class ChenZhen():
    def lianHuanTui(self):
        print('连环腿')


class HuoDongGe(HuoYuanJia, ChenZhen):
    pass


h1 = HuoDongGe()
h1.huoJiaTui()
h1.huoJiaQuan()
h1.lianHuanTui()
