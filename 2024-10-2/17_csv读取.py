# 导入csv模块
import csv

csv_path = r'/2024-10.2\data\学员登记表'
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 3:
            print(f'{row[0]}--{row[1]}--{row[2]}')
