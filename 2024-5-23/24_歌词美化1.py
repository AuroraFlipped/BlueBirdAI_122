str = '''
“ when I Was Young i'd listen to the Radio ”
“   waiting for My Favorite songs ”
“ when They played i'd sing Along ”
“       it Made me Smile ”
'''
str1 = str.lower().strip().replace('when', 'When').replace('waiting', 'Waiting').replace('i\'d', 'I\'d').replace(
    '“', '').replace('”', '').strip()
print(str1)
