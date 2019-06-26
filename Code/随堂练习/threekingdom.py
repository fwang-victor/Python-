import jieba

file = 'G:\\personal_data\\PythonCode\\Data\\threekingdoms.txt'
with open(file,'r',encoding='utf-8') as f:
    txt = f.read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1 

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print('{0:>10}-->{1:5d}'.format(word,count))

