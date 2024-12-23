# 计算每月共多少天
# 获取年月信息
year = int(input('请输入以为四位数的年：'))
month = int(input('请输入一个两位数的月：'))
if 1000 <= year <= 9999 and 0 < month <= 12:
    if month == 4 or month == 6 or month == 9 or month == 11:
        print(f'{year}年{month}月一共：30天')
    elif month == 2:
        # 年份能被4整除并且不能被100整除，或者能被400整除
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f'{year}年{month}月一共：29天')
        else:
            print(f'{year}年{month}月一共：28天')
    else:
        print(f'{year}年{month}月一共：31天')
else:
    print('年或者月输入有误')