### Requests笔记

#### Response对象的属性

|属性|说明|
|--|--|
|r.status_code|http请求的返回状态，200表示连接成功，404表示失败|
|r.text|http响应内容的字符串形式，即URL对应的页面内容|
|r.encoding|从http header中猜测的响应内容编码方式|
|r.apparent_encoding|从内容中分析出的响应内容编码方式|
|r.content|http响应内容的二进制形式|

#### Requests库的7个主要方法

|方法|说明|
|--|--|
|requests.request()|构造一个请求，支撑以下各种方法的基础方法|
|requests.get()|获取html网页的主要方法|
|requests.head()|获取HTML网页头信息的方法|
|requests.post()|向HTML网页提交post请求的方法|
|requests.put()|向HTML网页提交put请求的方法|
|requests.patch()|向HTML网页提交局部修改请求|
|requests.delete()|向HTML页面提交删除请求| 

#### http协议对资源的操作

|方法|说明|
|--|--|
|GET|请求获取URL位置的资源|
|HEAD|请求获取URL位置资源的响应消息报告，即获得该资源的头部信息|
|POST|请求向URL位置的资源后附加新的数据|
|PUT|请求向URL位置存储一个资源，覆盖原URL位置的资源|
|PATCH|请求局部更新URL位置的资源，即改变该出资源的部分内容|
|DELETE|请求删除URL位置存储的资源|

#### requests.request(method,url,**kwargs)

method:请求方式，对应get/put/post等
url:获取页面的URL链接
**kwargs:控制访问的参数：

* params:字典或字节序列，作为参数增加到URL中
* data:字典、字节序列或文件对象，作为request的内容
* json:json格式的数据，作为request的内容
* headers:字典，http定制头
* cookies：字典或cookiejar，request中的cookie
* auth： 元组，支持认证功能
* files：字典类型，传输文件
* timeout：设定超时时间，以秒为单位
* proxies:字典类型，设定访问代理服务器，可以增加登录认证
* allow_redirects:True/False,默认为True，重定向开关
* stream：True/False,默认为True，获取内容立即下载开关
* verify: True/False,默认为True，认证SSL证书开关
* cert：本地SSL证书路径 

---

requests.get(url,params=None,**kwargs)
requests.post(url,data=None,json=None,**kwargs)

