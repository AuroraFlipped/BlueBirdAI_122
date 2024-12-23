def jisuan(x, y):
    zhouchang = 2 * (x + y)
    mianji = x * y
    return zhouchang, mianji
    # 这样写返回值为一个元组


chang = float(input('请输入长方形的长：'))
kuan = float(input('请输入长方形的宽：'))
result = jisuan(chang, kuan)
# 返回值为一个元组
print(result)
print(f'周长为：{result[0]}面积为：{result[1]}')
