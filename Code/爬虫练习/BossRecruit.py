import requests 
from bs4 import BeautifulSoup

def getHtmlText(url,keyword_search,page=0,timeout=10):
    payload = {'query':keyword_search,'page':page}
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    try:
        print(f'现在爬取第{page+1}页数据')
        r = requests.get(url,params=payload,headers=header)
        print(f'连接状态{r.status_code}')
        r.raise_for_status 
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'failed'

def parsePage(html):
    info = []
    soup = BeautifulSoup(html,'html.parser') 
    job_list = soup.find('div',class_='job-list')
    for lst in job_list.find_all('div',class_ ='job-primary'):
        job_title = lst.find('div',class_ = 'job-title').string
        salary = lst.find('span',class_ = 'red').string
        company = lst.find('div',class_ = 'company-text').string
        info.append((job_title,salary,company))
    return info


def main():
    url = 'https://www.zhipin.com/c101210100/'
    keyword_search = 'python'
    num = 1
    for i in range(num):
        html = getHtmlText(url,keyword_search,i)
        data = parsePage(html)
        print(data)
        
    
main()


