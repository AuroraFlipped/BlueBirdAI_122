# 一山兔子，一山鸡，属头3600，属腿11000，通过编程计算出共有多少支兔子多少只鸡
for i in range(1, 3600):
    for j in range(1, 3600):
        if i + j == 3600 and (i * 2) + (j * 4) == 11000:
            print(f'鸡有{i}只\t兔子有{j}只')
