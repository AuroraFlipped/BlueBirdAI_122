def calc_days(y, m):
    if m in [4, 6, 9, 11]:
        days = 30
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            days = 29
        else:
            days = 28
    else:
        days = 31
    return days


year1 = int(input('请输入年份：'))
month1 = int(input('请输入月份：'))
tian = calc_days(year1, month1)
print(f'{year1}年{month1}月应为{tian}天')
