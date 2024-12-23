str1 = '''
桃之夭夭，灼灼其华。 
之子于归，宜其室家。 
桃之夭夭，有蕡其实。 
之子于归，宜其家室。 
桃之夭夭，其叶蓁蓁。 
之子于归，宜其家人。
'''
# 设计字典装载统计数值：key:汉字字符或标点 value:汉字现现次数
count = {}
# 替换掉换行
str1 = str1.replace('\n', '')
# 替换空格
str1 = str1.replace(' ', '')
print(str1)
for n in str1:
    if n not in count:
        count[n] = 1  # 添加
    else:
        count[n] += 1  # 更新
for k, v in count.items():
    print(f'{k}出现了{v}次')
