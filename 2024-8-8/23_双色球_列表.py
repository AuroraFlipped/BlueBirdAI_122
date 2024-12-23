from random import randint as rd
redballs = []
while len(redballs) < 6:
    redall = rd(1,33)
    if redall not in  redballs:
        redballs.append(redall)
blueball = rd(1,16)
redballs.sort()
print(f'双色红球为{redballs}双色蓝球为{blueball}')