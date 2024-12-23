filepath = r'/2024-10.2\data\daily.text'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines, type(lines))
    for line in lines:
        print(line)
