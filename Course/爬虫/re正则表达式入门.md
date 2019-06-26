### 正则表达式笔记
raw string(原生字符串类型)
原生字符串类型与字符串类型的区别：
> 不包含转义符的字符串,只需要在字符串前加`r`

#### 功能函数
|函数|说明|
|--|--|
|re.search()|在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象|
|re.match()|从一个字符串的开始位置匹配正则表达式，返回match对象|
|re.findall()|搜索字符串，以列表类型返回全部能匹配的子串|
|re.split()|将一个字符串按照正则表达式匹配结果进行分割，返回列表类型|
|re.finditer()|搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象|
|re.sub()|在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串|

`re.search(pattern,string,flags=0)`
* pattern:正则表达式的字符串或原生字符串
* string:待匹配字符串
* flags: 正则表达式使用时的控制标记 

|常用标记|说明|
|--|--|
|re.I re.IGNORECASE|忽略正则表达式的大小写，[A-Z]能够匹配小写字符|
|re.M re.MULTILINE|正则表达式中的^操作符能够将给定字符串的每行当做匹配开始|
|re.S re.DOTALL|正则表达式中的.能够匹配所有字符，默认匹配除换行外的所有字符|

`re.split(pattern,string,maxsplit=0,flags=0)`
* maxsplit作为最大分割数，剩余部分作为最后一个元素输出 

`re.sub(pattern,repl,string,count=0,flags=0)`
* repl是用来替换的字符串，count为替换次数

#### re库的另一种等价用法 
re库的函数式用法为一次性操作，还有一种面向对象用法，可在编译后多次操作 
`regex = re.compile(pattern,flags=0)` 
通过compile生成的regex对象才能被叫做正则表达式 
#### re库的match对象 
match对象的属性 
|属性|说明|
|--|--|
|.string|待匹配的文本|
|.re|匹配时使用的pattern对象|
|||

match对象的方法 
|方法|说明|
|--|--|
|.group(0)|获得匹配后的字符串|
|.start()|匹配字符串在原始字符串的开始位置|
|.end()|匹配字符串在原始字符串的结束位置|
|.span()|返回(.start(), .end())|