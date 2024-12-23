# 用户登录验证。验证次数最多3次

cishu = 3
i = 0
while i <= 3:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    i += 1
    sheng = cishu - i
    if sheng == 0:
        break
    if username == '张三' and password == '123456789':
        print('欢迎张三登录成功')
    else:
        print(f'输入错误，你还有{sheng}次')

