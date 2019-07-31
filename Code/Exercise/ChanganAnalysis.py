import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
from snownlp import SnowNLP

path1 = 'D:/personal_data/python_code/PythonCode/Data/data7645/cities.csv'
path2 = 'D:/personal_data/python_code/PythonCode/Data/data7645/comments.csv'
df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
df = pd.merge(df1,df2,left_index=True,right_index=True,how='outer')
print(df.head(10))

#数据处理
df.loc[df['city'] == '--','city'] = np.nan
new_df = df.dropna()
city_count = new_df['city'].value_counts().sort_values(ascending=False).iloc[:10]
print(city_count)

#数据绘图
plt.figure()
plt.bar(np.arange(len(city_count)),city_count.values)
plt.title('长安十二时辰观众城市分布',fontproperties='SimHei')
plt.xlabel('city')
plt.ylabel('number')
plt.xticks(np.arange(len(city_count)),city_count.index,fontproperties='SimHei')
#plt.show()

#词云绘制
comment_cut = ''
comments = df['comment'].tolist()
for comment in comments:
    comment = jieba.cut(comment)
    comment = ' '.join(comment)
    comment_cut += comment
stopwords = STOPWORDS.copy()
stopwords.update([
    '长安', '十二', '这种', '完全', '最后', '但是', '这个', '还是','时辰','千玺'
    '有点', '电影', '希望', '没有', '就是', '什么', '觉得', '其实',
    '不是', '真的', '感觉', '因为', '这么', '很多', '已经', '一个',
    '这样', '一部', '非常', '那么', '作为', '个人', '基本', '只能',
    '真是', '应该', '不能', '尤其', '可能', '确实', '只是', '一点',
])
wc = WordCloud(width=1024,height=768,max_font_size=400,max_words=100,font_path='msyh.ttf',
               stopwords=stopwords)
wc.generate(comment_cut)
#wc.to_file('wordcloud.png')

#情感分析
motion_list = []
for i in df['comment']:
    try:
        s = round(SnowNLP(i).sentiments,2)
        motion_list.append(s)
    except:
        continue

result = {}
for i in set(motion_list):
    result[i] = motion_list.count(i)

attr1, val1 = [], []
info = result
info = sorted(info.items(), key=lambda x: x[0], reverse=False)
for each in info[:-1]:
    attr1.append(each[0])
    val1.append(each[1])

plt.style.use('ggplot')
plt.figure(figsize=(20, 4))
plt.plot(attr1, val1)
plt.title('观众情感分析',fontproperties='SimHei')
plt.show()

