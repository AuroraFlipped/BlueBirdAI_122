# 编写程序，输入一个18位的身份证号码，从中提取出生日期，并以“出生日期是*年*月*日”样的
# 格式输出。
ID_number = input('请输入18为有效身份证号：')
nian = ID_number[6:10]
yue = ID_number[10:12]
ri = ID_number[12:14]
print(f'出生日期是{nian}年{yue}月{ri}日')
