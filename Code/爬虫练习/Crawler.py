import requests
from pyquery import PyQuery 

urls = ['https://movie.douban.com/subject/1292052/',
'https://movie.douban.com/subject/1962665/',
'https://movie.douban.com/subject/26752088/']

def Get_Text(url):
    response = requests.get(url)
    Text = response.text
    return Text   

def Write_csv(Text):
    Text = PyQuery(Text)
    title = Text.find('#content > h1 > span:nth-child(1)').text()
    year = Text.find('#content > h1 > span.year').text()
    with open('cral.txt','a') as cral_file:
        cral_file.write(title)
        cral_file.write(year)

if __name__ == '__main__':
    for url in urls:
        Text = Get_Text(url)
        Write_csv(Text)



