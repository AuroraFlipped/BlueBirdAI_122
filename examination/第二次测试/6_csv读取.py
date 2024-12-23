import csv

filepath = r'D:\ST\Code\BluAIPycharmProject\examination\第二次测试\通讯录.text'
with open(filepath, mode='r', encoding='utf-8') as f:
    readers = csv.reader(f)
    for row in readers:
        if row == 0:
            print(row[0])