class HuoYuanJia():
    def huoJiaQuan(self):
        # print('霍家拳')
        s ='霍家拳'
        return s
    def huoJiaTui(self):
        print('霍家腿')


class ChenZhen():
    def lianHuanTui(self):
        print('连环腿')


class HuoDongGe(HuoYuanJia, ChenZhen):
    # def HuoJiaQuan(self):
    def shuangJieGun(self):
        # 通过下面两种方式可以使子类在内部使用父类
        # super().HuoJiaQuan() #parent
        # HuoYuanJia.huoJiaQuan(self)

        str1 = HuoYuanJia.huoJiaQuan(self)
        # 重写
        str1 = str1 + 'hahahengha'
        print(str1)
        return str1
    pass


h1 = HuoDongGe()
a = h1.shuangJieGun()
print(a)
