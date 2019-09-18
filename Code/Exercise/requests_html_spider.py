from requests_html import HTMLSession
import  requests_html

session = HTMLSession()


class GetPage:
    def __init__(self,url,header):
        self._url = url
        self._headers = header

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers

    # @url.setter
    # def url(self,url):
    #     self._url = url
    #
    # @headers.setter
    # def headers(self,header):
    #     self._headers = header

    def get_page(self):
        try:
            _resp = session.get(self._url,headers = self._headers)
            if _resp.status_code == 200:
                return _resp.html
            else:
                return None
        except Exception as e:
            print(e)

    def parse_css(self,response):
        lst = []
        if isinstance(response,requests_html.HTML):
            items = {}
            for item in response.find('div.indent > div > table '):
                #print(item.html)
                items['movie_name'] = item.find('tr > td:nth-child(2) > div > a',first=True).text.strip()
                items['introduction'] =item.find('p',first=True).text.strip()
                items['score'] = item.find('.rating_nums',first=True).text.strip()
                items['number_of_people'] = item.find('span:nth-child(3)',first=True).text.strip()
                lst.append(items)
        return lst



    def parse_xpath(self,response):
        lst = []
        if isinstance(response,requests_html.HTML):
            items = {}
            for item in response.xpath(''):
                items['movie_name'] = item.xpath()
                items['introduction'] = item.xpath()
                items['score'] = item.xpath()
                items['number_of_people'] = item.xpath()
                lst.append(items)
        return lst




if __name__ == '__main__':
    url = 'https://movie.douban.com/chart'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    douban = GetPage(url,header)
    html = douban.get_page()
    print(douban.parse_css(html))




