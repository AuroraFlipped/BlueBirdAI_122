# 导入random库，实现随机取数
import random
# 取随机数赋值给num_rand
num_rand = random.randint(1, 10)
# 获取用户输入数
num = input('请输入四位数字')
# 判断num字符串中是否都是数字，第一个数字是否为0
if num.isdigit() and int(num[0]) != 0 and len(num) == 4:
    # if num.isdigit ==True  and (num[0]) != '0':
    num_baiwei = (int(num) // 100) % 10
    print(f'百位数字：{num_baiwei}\t中奖数字：{num_rand}')
    if num_baiwei == num_rand:
        print('恭喜你中奖了')
    else:
        print('很遗憾你没有中奖')
else:
    print('你输入的不符合要求，非四位有效数字')
