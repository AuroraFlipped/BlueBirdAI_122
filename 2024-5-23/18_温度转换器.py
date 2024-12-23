# 练习温度转换器
# 转换公式 摄氏度=5/9.0*(华氏度-32)
Fahrenheit = float(input("请输入你的华氏度:"))
Celsius = int(5 / 9.0 * (Fahrenheit - 32))
print('-' * 10, '温度转换器', '-' * 10)
print('华氏温度', '\t\t', '摄氏温度')
print(f'{Fahrenheit}\t\t\t\t{Celsius}')
print('-' * 31)
