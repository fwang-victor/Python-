import requests 
import re 
from bs4 import BeautifulSoup 

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=10)
        r.raise_for_status 
        r.encoding = r.apparent_encoding 
        return r.text
    except:
        return 'failed'

def getStockList(lst,stockURl):
    html = getHTMLText(stockURl)
    soup = BeautifulSoup(html,'html.parser')
    a= soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][zh]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL + stock +'.html'
        html = getHTMLText(url)
        try:
            if html =='':
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockinfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockinfo
    


def main():
    stock_list_url =''
    stock_info_url =''


main()
