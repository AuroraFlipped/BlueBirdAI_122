# 返回值元组
def nianjia(workyear):
    if workyear < 5:
        yearjia = 1
    elif workyear >= 5 and workyear < 10:
        yearjia = 5
    else:
        yearjia = 7
    return yearjia


n = int(input('请输入你的工龄：'))
result = nianjia(n)
print(f'您的年假为{result}天')
