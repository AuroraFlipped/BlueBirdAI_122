# 编写程序，产生两个0~100之间的随机整数a和b,然后比较大小，并提示输出二个随机数分别为a,b 的值，输出最大的那个值

from random import randint as rd

a = rd(1, 100)
b = rd(1, 100)
max_ = a if a > b else b
print(f'a的值为{a}\tb的值为{b}\t最大值{max_}')
