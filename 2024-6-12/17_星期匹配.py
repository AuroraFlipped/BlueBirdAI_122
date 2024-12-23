'''
从键盘输入一位整数，当输入 1~7 时，显示对应的英文星期缩写，输入其他数字时提示 用户重新输入，输入数字 0 时程序结束。其中 1 对应 MON、2 对应 TUE、3 对应 WED、4 对 应 THU、5 对应 FRI、6 对应 SAT、7 对应 SUN。
'''

while True:
    week = input("请输入1-7,0可就退出了")
    if week == '0':
        break
    elif week == '1':
        print('mon')

    elif week == '2':
        print('tue')

    elif week == '3':
        print('wed')

    elif week == '4':
        print('thu')

    elif week == '5':
        print('FRI')

    elif week == '6':
        print('sat')

    elif week == '7':
        print('thu')
    else:
        print('输入有误！')
