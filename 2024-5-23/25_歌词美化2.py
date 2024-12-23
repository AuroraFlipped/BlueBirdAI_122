# 歌词美化练习参考后
word1 = 'when i Was Young i\'d listen to the Radio '
word2 = '   waiting for My Favorite songs    '
word3 = '    when They played i\'d sing Along   '
word4 = '           it Made me Smile '
word1 = word1.strip().replace('when', 'When').replace('i', 'I', 2)  # 其中2为替换的次数
word2 = word2.strip().replace('waiting', 'Waiting')
word3 = word3.strip().replace('when', 'When').replace("i'd", "I'd")  # 这里可以换成双引来完成其中的'也可以使用\'来转义完成
word4 = word4.strip().replace('it', 'It')
print(word1, word2, word3, word4, sep='\n')
