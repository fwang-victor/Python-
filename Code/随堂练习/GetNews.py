import requests  
from lxml import etree
from apscheduler.schedulers.blocking import BlockingScheduler
import jieba
from wordcloud import WordCloud 
import time 


def GetNews():
    url = 'https://news.baidu.com/'
    session = requests.Session()
    response = session.get(url)
    html = etree.HTML(response.text)
    titles = html.xpath('//*[@id="pane-news"]/ul/li/a/text()')
    word_jieba = jieba.cut(''.join(titles),cut_all=True)
    word_split = ' '.join(word_jieba)
    my_wordcloud = WordCloud(background_color='black',font_path='C:\Windows\Fonts\simhei.ttf',
        max_words = 100,width = 1600,height = 800)
    my_wordcloud = my_wordcloud.generate(word_split)
    now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    my_wordcloud.to_file(now+'.png')

 

if __name__ == '__main__':
    #sched = BlockingScheduler()
    #sched.add_job(GetNews,'interval',seconds=5)
    #sched.start()
    GetNews()
    

    