# 编写程序，使用循环语句输出1+4+7+10+13+…+112的和
sum = 0
for i in range(1, 113, 3):
    sum += i
print(sum)
