import requests
from bs4 import BeautifulSoup
import bs4
import traceback
import pandas as pd
import time


def getHTMLText(url):
    try:
        s =  requests.Session()
        s.get('http://q.10jqka.com.cn/')
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Referer':'http://data.10jqka.com.cn/financial/yjyg/'}
        r = s.get(url,timeout=10,headers = header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return 'failed'

def pageParse(html,info):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').contents:
        if isinstance(tr,bs4.element.Tag):
            tds = tr.find_all('td')
            rank = tds[0].string
            code = tds[1].text.strip()
            secname = tds[2].text.strip()
            yjtype = tds[3].text.strip()
            title = tds[4].text.strip()
            yjrange = tds[5].string.strip()
            declaredate = tds[7].string.strip()
            info.append([rank,code,secname,yjtype,title,yjrange,declaredate])
    return info


def printStock(info):
    df = pd.DataFrame(info,columns=['序号','股票代码','证券简称','业绩预告类型','摘要','变动幅度','公告日期'])
    #df.to_csv('yjyg.csv',sep=',',header=False,index=False)
    df.to_excel('yjyg.xlsx',sheet_name='sheet1',header=True,index=False)



def main():
    num = 10
    report = '2019-06-30'
    lst = []
    start_time = time.perf_counter()
    for i in range(1,num+1):
        url = 'http://data.10jqka.com.cn/ajax/yjyg/date/{0:s}/board/ALL/field/enddate/order/desc/page/{1:d}/'.format(report,i)
        a = 2 * i * '*'
        b = 2* (num-i) * '-'
        c = (i/num)*100
        dur = time.perf_counter() - start_time
        print('\r{:4.2f} %{}->{}{:2f}'.format(c,a,b,dur),end='')
        html = getHTMLText(url)
        data = pageParse(html,lst)
    printStock(lst)

main()
print('\n'+'执行结束'.center(20,'-'))



