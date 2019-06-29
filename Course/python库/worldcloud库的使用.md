* 安装 
> `pip install worldcloud`
#### 
worldcloud.WorldCloud()代表一个文本对应的词云

> `w = worldcloud.WorldCloud()`

|方法|描述|
|--|--|
|w.generate(txt)|向WorldCloud对象中加载文本|
|w.to_file(filename)|将词云输出为图像文件|

#####词云绘制步骤
* 配置对象参数
* 加载词云文本
* 输出词云文件 

|参数|描述|
|--|--|
|width|指定词云对象生成图片的宽度|
|height|指定词云对象生成图片的高度|
|min_font_size|指定词云中字体的最小字号|
|max_font_size|指定词云中字体的最大字号，根据高度自动调节|
|font_step|字体字号的步进间隔|
|font_path|指定字体文件的路径，默认为None，中文可以使用'msyh.ttc'|
|max_words|词云显示的最大单词数量|
|stop_words|词云的排除词列表，即不显示的单词列表|
|mask|指定词云形状，默认为长方形，需要引入imread()函数|
||`from scipy.misc import imread`|
||`mk = imread('pic.png')`|
||`w = worldcloud.WorldCloud(mask=mk)`|
|background_color|指定词云图片的背景颜色，默认为黑色|
