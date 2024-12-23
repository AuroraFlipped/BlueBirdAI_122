'''
需求
用户输入四位有效数字，百位上的数字等于系统随机产生的一个数字
eg：
如果客户输入1234，那么百位为2
如果随机数为2，那么中奖了
'''
import random

number = int(input('请输入四位数字'))
luckynumber = random.randint(0, 9)
baiwei = number % 1000 // 100
# baiwei = number // 100 % 10
print(f'百位数字{baiwei}\t幸运数字{luckynumber}')
if luckynumber == baiwei:
    print('恭喜你中了两个亿')
else:
    print('很遗憾你错了两个亿')
