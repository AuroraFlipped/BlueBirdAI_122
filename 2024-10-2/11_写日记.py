# 1. 客户输入q退出
# 2. 把内容存到列表当中
# 3. 把内容保存到2024-10-2\daily.text 当中
filepath = r'/2024-10.2\data\daily.text'
contents = []
while True:
    line = input('输入q保存退出')
    if line.lower() == 'q':
        break
    contents.append(line + '\n')
f = open(filepath, 'w', encoding='utf-8')
f.writelines(contents)
f.close()
print(f'文件{filepath}成功')
