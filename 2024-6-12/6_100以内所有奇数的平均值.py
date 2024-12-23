# 100以内所有奇数的平均值

i = 1
sum = 0
count = 0
while i <= 100:
    if i % 2 == 1:
        sum = sum + i
        count = count + 1
    i = i + 1
average = sum / count
print(count)
print(average)
