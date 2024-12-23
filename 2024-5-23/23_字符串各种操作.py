# 字符串的各种操作
string = ' 我喜欢Dance '
print(string.lower())  # 全部换成小写
print(string.upper())  # 全部换成大写
print(string.lstrip())  # 去除开头空格
print(string.rstrip())  # 去除末尾空格
print(string.strip())  # 去除首尾空格
print(string.split('欢'))  # 指定从某个字符拆分
print(string.find('D'))  # 查找某个字符如果数多个相同的只会返回第一次出现的位置如果是找不到的则会返回-1
print(string.replace('D', 'G'))  # 指定替换某个字符
print(len(string))  # 查看字符串的长度
