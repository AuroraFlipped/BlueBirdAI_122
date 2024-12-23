from random import randint as rd

# 生成蓝球
blue = rd(1, 16)
# 通过集合存红球
reds = set()
while True:
    r = rd(1, 33)
    reds.add(r)
    if len(reds) == 6:
        break
reds = list(reds)
reds.sort()
print('红球', end='')
for i in range(len(reds)):
    print(reds[i], end=' ')
print('蓝球', blue)
