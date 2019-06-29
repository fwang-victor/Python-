def getText(file):
    with open(file,'r') as f:
        txt = f.read()
        txt = txt.lower()
    for ch in ",./?;:'[]-!@#$%^&*()+=|":
        txt = txt.replace(ch,' ')
    return txt 


if __name__ == "__main__":
    file = 'hamlet.txt'
    txt = getText(file)
    words = txt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse= True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10} {1:>}".format(word,count))

