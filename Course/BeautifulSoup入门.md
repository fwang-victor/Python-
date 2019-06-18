### BeautifulSoup笔记

from bs4 import BeautifulSoup

#### BeautifulSoup库解析器
|解析器|使用方法|条件|
|--|--|--|
|bs4的HTML解析器|BeautifulSoup(mk,'html.parser')|安装bs4库|
|lxml的HTML解析器|BeautifulSoup(mk,'lxml')|pip install lxml|
|lxml的XML解析器|BeautifulSoup(mk,'xml')|pip install lxml|
|html5lib的解析器|BeautifulSoup(mk,'html5lib')|pip install html5lib|

####  BeautifulSoup类的基本元素
|基本元素|说明|
|--|--|
|Tag|标签，最基本的信息组织单元，分别用<></>标明开头和结尾|
|Name|标签的名字 `<p></p>`的名字是'p'，格式:`<tag>.name`|
|Attributes|标签的属性，字典形式组织，格式：`<tag>.attrs`|
|NavigableString|标签内非属性字符串，`<>...</p>`中字符串，格式：`<tag>.string`|
|Comment|标签内字符串的注释部分，一种特殊的Comment类型|
#### html内容遍历方法
标签树的下行遍历
|属性|说明|
|--|--|
|.contents|子节点的列表,将`<tag>`所有儿子节点存入列表,'\n'也是儿子节点|
|.children|子节点的迭代类型，与.contents类似，用于循环遍历儿子节点|
|.descendants|子孙节点的迭代类型，包含所有子孙节点，用于循环遍历|
标签树的上行遍历 
|属性|说明|
|--|--|
|.parent|节点的父亲标签|
|.parents|节点先辈标签的迭代类型，用于循环遍历先辈节点,会遍历到soup本身|
标签树的平行遍历
|属性|说明|
|--|--|
|.next_sibling|返回按照HTML文本顺序的下一个平行节点标签|
|.previous_sibling|返回按照HTML文本顺序的上一个平行节点标签|
|.next_siblings|迭代类型，返回按照HTML文本顺序的后续所有平行节点标签|
|.previous_siblings|迭代类型，返回按照HTML文本顺序的前序所有平行节点标签|
#### 信息提取的一般方法
#### HTML内容查找方法
<>.find_all(name,attrs,recursive,string,**kwargs)
返回一个列表类型，存储查找的结果 
* name:对标签名称的检索字符串,可以传入一个标签名称，也可以传入一个名称列表，如果传入参数为True，则查找所有标签。
* attrs:对标签属性值的检索字符串，可标注属性检索 

