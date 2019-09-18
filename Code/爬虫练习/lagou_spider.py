from requests_html import HTMLSession
import requests_html
import time
import json
import csv



class LagouSpider(object):
    def __init__(self):
        self.url_init = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
        self.search_positon = '数据分析'
        self.page = 1
        # self.formdata = {
        #     'pn':self.page,
        #     'kd':self.search_positon
        # }
        self.headers = {
            'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
        }

    def __setpage__(self):
        self.page += 1
        return self.page

    def get_page(self):
        session = HTMLSession()
        r = session.get(self.url_init,headers=self.headers)
        r_cookies = r.cookies
        try:
            print('正在爬取第{}页'.format(self.page))
            resp = session.post(self.url,data={'pn':self.page,'kd':self.search_positon},headers=self.headers,cookies=r_cookies)
            if resp.status_code == 200:
                self.__setpage__()
                return resp.html
        except Exception as e:
            print(e)
            return None

    def page_parse(self,response):
        if isinstance(response,requests_html.HTML):
            data = json.loads(response.text)
            Item = {}
            for job in data['content']['positionResult']['result']:
                Item['companySize'] = job['companySize']
                Item['companyLabelList'] = ','.join(job['companyLabelList'])
                Item['workYear'] = job['workYear']
                Item['education'] = job['education']
                Item['positionName'] = job['positionName']
                Item['salary'] = job['salary']
                Item['companyShortName'] = job['companyShortName']
                Item['companyFullName'] = job['companyFullName']
                yield Item

    def data_csv(self,filename):
        try:
            html = self.get_page()
            datas = self.page_parse(html)
            fieldname = ['companySize','companyLabelList','workYear','education','positionName','salary','companyShortName','companyFullName']
            with open(filename,'a',newline='',encoding='utf-8') as f:
                writer = csv.DictWriter(f,fieldnames=fieldname)
                #riter.writeheader()
                for item in datas:
                    writer.writerow(item)
            time.sleep(3)
            while self.page <= 30:
                self.data_csv(filename)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.data_csv('lagou.csv')
    print('爬取完成')






