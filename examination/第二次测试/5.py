
from examination.第二次测试.data.menu import *

while True:
    menu = input('1.添加联系人2.查找联系人3.删除联系人4.修改联系人输入0退出')
    if menu == '0':
        break
    elif menu == '1':
        name = input('请输入联系人姓名：')
        salary = input('请输入薪资：')
        add_tongxun(name, salary)
    elif menu == '2':
        check_tongxun()
    elif menu == '3':
        name = input('请输入要删除的姓名：')
        delete_tongxun(name)
    elif menu == '4':
        name = input('请输入修改人姓名：')
        update_tongxun(name)
