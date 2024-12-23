# if-else 结构
# 如果是晴天，就外出游玩，否则就去游泳
weather = input('请输入天气状况：')
if weather == '晴天':
    print('外出游玩')
else:
    print('游泳')
# 输入性别是男性就嫁给你，否则就不嫁
sex = input('请输入您的性别：')
if sex == '男':
    print('嫁给你')
else:
    print('不嫁')
# 本月销售业绩金额小于 500000，则输出“业绩低，无提成”，否则输出“业绩达标， 有提成”
sale = float(input('请输入您业绩金额：'))
if sale <= 500000:
    print('业绩低，无提成')
else:
    print('业绩达标，有提成')
# 输入一个数字，判断是否为偶数
number = float(input('请输入一个数：'))
if number % 2 == 0:
    print('您输入的数为偶数')
else:
    print('您输入的不是偶数')
