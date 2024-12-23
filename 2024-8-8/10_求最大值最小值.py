def check_input():


    while True:
        num = input('请输入一个数：')
        if num.isdigit() == True:
            break
    v = int(num)
    return v
# print(checkinput())
n = 5
numbers = []
for i in range(n):
    result = check_input()
numbers.append(result)
print(f'最大值{max(numbers)}最小值{min(numbers)}')
