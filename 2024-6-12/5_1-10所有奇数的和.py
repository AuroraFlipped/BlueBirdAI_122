# # 计算1-10所有奇数的和
# i = 1
# sum = 0
# while i < 10:
#     sum = sum + i
#     i += 2
# print(sum)

sum = 0  # 初始化和
i = 1  # 初始化变量
while i <= 10:
    i = i + 1
    # 判断是否是奇数
    # if i % 2 != 0:
    if i % 2 == 1:
        sum = sum + i
print('1~10所有的奇数和为：', sum)
