import os
from os import path
import  numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import time
import re
import multidict

def MakeImage(text):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    alice_mask = np.array(Image.open(path.join(d,'background.jpg')))
    wc = WordCloud(background_color='white',max_words=100,mask=alice_mask,
                   max_font_size=200,scale=2)
    wc.generate_from_frequencies(text)
    wc.to_file(path.join(d,'english_fre.png'))
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

def GetFrequencyText(sentence):
    fulldict = multidict.MultDict()
    tmpdict = {}

    for text in sentence.split(" "):
        if re.match("",text):
            continue
        val = tmpdict.get(text,0)
        tmpdict[text.lower()] = val+1
    for key in tmpdict:
        fulldict.add(key,tmpdict[key])
    return fulldict

d = path.dirname(__file__)

text = open(path.join(d,'english.txt')).read()
MakeImage(GetFrequencyText(text))
