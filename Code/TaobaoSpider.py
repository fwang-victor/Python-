import requests 
import re 

def getHtmlText(url,search,num,timeout=10):
    payload = {'q':search,'data-value':str(num*44)}
    try:
        print('开始爬取第{:^3}页数据'.format(num+1))
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        r = requests.get(url,params=payload,headers=header)
        print(r.status_code)
        print('当前爬取网址为:{}'.format(r.url))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text 
    except:
        return '爬取失败'

def parsePage(html,lst):
    try:
        tlt = re.findall(r'"raw_title":".*?"',html)
        plt = re.findall(r'"view_price":"[\d.]+"',html)
        for i in range(len(plt)):
            title = eval(tlt[i].split(':')[1])
            price = eval(plt[i].split(':')[1])
            #lst.append((title,price))
            #print(title,price)
        #return lst
    except:
        return 'parse failed'


def main():
    url = 'https://s.taobao.com/search'
    search = 'iphone'
    num = 2
    info = []
    for i in range(int(num)):
        html = getHtmlText(url,search,i)
        data = parsePage(html,info)
        print(html)


main()


