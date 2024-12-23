# 编程,任意输入5个数,找出最小数.
number = int(input('请任意输入一个有效数字：'))
min_ = number
i = 1
while i < 5 :
    i += 1
    if number < min_ :
        min_ = number
    number = int(input('请任意输入一个有效数字：'))
print(f'最小数为{min_}')



