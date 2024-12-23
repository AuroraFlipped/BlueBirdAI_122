yang = []
for i in range(1, 9):
    sublist = [1] * i
    yang.append(sublist)
# j 代表行
for j in range(2, len(yang)):
    list3 = yang[j]
    # i 代表列
    for i in range(len(list3)):
        if i == 0 or i == len(list3) - 1:
            continue
        list3[i] = yang[j - 1][i] + yang[j - 1][i - 1]
for i in range(len(yang)):
    sublist = yang[i]
    print(sublist)
