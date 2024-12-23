# # 使用随机数模块生成双色球号码
# 双色球规则：
# • 红球：6 个，红球的号码范围 1~33
# • 篮球：1 个，篮球的号码范围 1~16
# • 红球以从小到大的顺序排列

from random import randint as rd

blueball = rd(1, 16)
redballs = []
i = 0
while i < 5:
    redball = rd(1, 33)
    redballs.append(redball)
    i += 1
redballs.sort()
print('红球为：', end='')
for i in redballs:
    print(i, end=' ')
print(f'蓝球为：{blueball}')
