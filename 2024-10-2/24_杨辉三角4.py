yang = []
for i in range(1, 9):
    sublist = [1] * i
    yang.append(sublist)
for i in range(2, len(yang)):
    list3 = yang[i]
    for i in range(len(list3)):
        if i == 0 or i == len(list3) - 1:
            continue
        list3[i] = 0
for i in range(len(yang)):
    sublist = yang[i]
    print(sublist)
