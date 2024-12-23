filepath = r'/2024-10.2\data\daily.text'
with open(filepath, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        print(line, end='')
