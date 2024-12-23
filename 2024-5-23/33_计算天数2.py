# 计算每月共多少天
year = int(input('请输入一个四位数的年：'))
month = int(input('请输入一个两位数的月份：'))
if (year >= 1000 and year <= 9999) and (month > 0 and month <= 12):
    if month in (4, 6, 9, 11):
        print(f'{year}年{month}月一共有30天')
    elif month == 2:
        # 年份能被4整除且不能被100整除或者能被400整除
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f'{year}年{month}月一共有28天')
        else:
            print(f'{year}年{month}月一共有29天')
    else:
        print(f'{year}年{month}月一共有31天')
