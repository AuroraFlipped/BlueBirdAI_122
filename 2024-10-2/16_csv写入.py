# 引入csv模块
import csv


csv_path = r'/2024-10.2\data\学员登记表'
# f = open(csv_path, 'a',encoding='utf-8')
# f.close()
# 相当于使用with
with open(csv_path, 'a', encoding='utf-8') as f:
    # csv写入对象
    write = csv.writer(f)
    name = input('请输入学员姓名：')
    age = input('请输入学员年龄：')
    sex = input('请输入学员性别：')
    write.writerow([name, age, sex])
