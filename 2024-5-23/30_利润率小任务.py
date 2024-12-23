'''需求：输入一个利润率，做一个利润率评价，给出在个等级。（优中差）如利润率大于0.3高利润, 利润率大于0低利润，否则是负利润
'''
# 利润率 = 利润 / 价格
price = float(input('商品价格：'))
profit = float(input('利润：'))
profit_rate = profit / price
if profit_rate > 0.3:
    print('高利润')
elif 0 < profit_rate < 0.3:
    print('正常')
else:
    print('低利润')
