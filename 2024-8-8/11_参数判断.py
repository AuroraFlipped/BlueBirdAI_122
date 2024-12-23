def intro(name, age, addr):
    if age < 6:
        print(f'我叫{name},我还是小朋友，家住{addr}')
    elif 6 <= age < 16:
        print(f'我叫{name},我是成人了，家住{addr}')
    elif age >= 16 and age < 60:
        print(f'我叫{name},我快老了，家住{addr}')
    else:
        print(f'我叫{name}, 我不知该说什么了，我快跑路了，家住{addr}')
intro('张三',2,'房山')
intro('张老三',128,'房山')
