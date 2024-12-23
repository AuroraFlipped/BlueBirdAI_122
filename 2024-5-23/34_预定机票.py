# 机票原价为
price = 5000
# 获取购买机票的月份
month = int(input('请输入你购买机票的月份：'))
# 获取乘客购买机票的舱型
level = input('请输入您的舱型（头等舱请输入1，经济舱输入2）：')
# 判断购买机票月份是否为旺季
if month in (4, 5, 6, 7, 8, 9, 10,):
    if level == '1':
        xian_price = price * 0.9
        print(xian_price)
    else:
        xian_price = price * 0.6
        print(xian_price)
else:
    if level == '1':
        xian_price = price * 0.5
        print(xian_price)
    else:
        xian_price = price * 0.4
        print(xian_price)
