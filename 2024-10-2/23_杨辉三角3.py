yang = []
for i in range(1, 9):
    subList = [1] * i
    yang.append(subList)
list3 = yang[2]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0
list3 = yang[3]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0
list3 = yang[4]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0
list3 = yang[5]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0
list3 = yang[6]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0
list3 = yang[7]
for i in range(len(list3)):
    if i == 0 or i == len(list3) - 1:
        continue
    list3[i] = 0

for i in range(len(yang)):
    print(yang[i])
