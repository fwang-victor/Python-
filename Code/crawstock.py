import requests
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url):
    try:
        s =  requests.Session()
        s.get('http://q.10jqka.com.cn/')
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Referer':'http://q.10jqka.com.cn/'}
        r = s.get(url,timeout=10,headers = header)
        #print('开始爬取第{}页内容'.format())
        #print(r.status_code)
        #print(r.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'failed'

def pageParse(html,info):
    soup = BeautifulSoup(html,'html.parser')
    try:
        for tr in soup.find_all('tr'):
            # 过滤标题行
            if tr('td'):
                tds = tr.find_all('td')
                rank = tds[0].string
                code = tds[1].string
                name = tds[2].string
                info.append((rank,code,name))
        return info
    except:
        traceback.print_exc()
        return 'parse failed'

def printStock(info):
    for i in info:
        print('序号:{0:4}股票代码:{1:10}股票名称:{2:}'.format(i[0],i[1],i[2]))

def main():
    num = 4
    url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/'
    lst = []
    for i in range(1,num):
        new_url = url + str(i)
        html = getHTMLText(new_url)
        data = pageParse(html,lst)
    printStock(lst)



main()
