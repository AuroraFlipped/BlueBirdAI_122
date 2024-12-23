# 输入一批整数，比较并输出其中最大值和最小值，输入数字0时结束循环。
number1 = int(input('请输入一个整数（输入0结束）：'))
max_ = min_ = number1
while number1 != 0:
    if number1 > max_:
        max_ = number1
    elif number1 < min_:
        min_ = number1
    number1 = int(input('请输入一个整数（输入0结束）：'))
print(f'最大值为{max_}最小值为{min_}')
