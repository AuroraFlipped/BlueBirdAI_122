# 输入一个整数，将整数的数字进行反转，例如输入 12345，输出 54321，运行效果如下 图所示。
num = input('输入一个整数：')
str_len = len(num)
for i in range(1, str_len + 1):
    index = i * -1
    print(num[index], end='')
