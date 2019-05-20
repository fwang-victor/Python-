import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud ,STOPWORDS,ImageColorGenerator

#获取源码所在的系统位置
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#获取文件内容
text = open(path.join(d,'english.txt')).read()
#获取背景遮罩形状
color = np.array(Image.open(path.join(d,'background.jpg')))
#设置要屏蔽的词
stopwords = set(STOPWORDS)
stopwords.add('said')

#mask遮罩图,stopwords屏蔽词,random_state 为每个单词返回一个PIL颜色
wc = WordCloud(background_color='white',max_words=100,mask=color,scale=2,
               stopwords=stopwords,max_font_size=200,random_state=42)
wc.generate(text)

#
#image_colors = ImageColorGenerator(color)

#show
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
wc.to_file(path.join(d,'wc_english.png'))
plt.figure()
plt.imshow(color,cmap='gray',interpolation='bilinear')
plt.axis('off')

plt.show()