from menu.menu_worek import *

while True:
    menu = input('1.添加 2.查看 3.修改 4. 删除 0退出')
    if menu == '0':
        break
    elif menu == '1':
        name = input('请输入姓名：')
        tel = input('请输入电话：')
        adduser(name, tel)
    elif menu == '2':
        checkuser()
    elif menu == '3':
        name = input('请输入要修改的的姓名：')
        updateuser(name)
    elif menu == '4':
        name = input('请输入要删除的姓名：')
        deleuser(name)
