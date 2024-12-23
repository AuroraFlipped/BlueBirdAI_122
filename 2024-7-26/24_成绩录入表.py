info = {}
while True:
    menu = input("输入1录入学生信息，输入2查看学生信息，输入0退出系统：")
    if menu == 0:
        break
    elif menu == 1:
        print("友情提示：学号为空直接退出")
        while True:
            if len(stuno) == 0:
                break
            stuno = input("请输入学生学号:")
            name = input("请输入学生姓名:")
            score = input("请输入学生成绩:")
            info['学号'] = stuno
            info['姓名'] = name
            info['成绩'] = score
    elif menu == 2:
        print("info")
