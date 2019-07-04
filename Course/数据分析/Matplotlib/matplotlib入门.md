matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式

`import matplotlib.pyplot as plt` 
> plt.plot(x,y)当有两个以上参数时，按照x轴和y轴顺序绘制数据点

>plt.axis()指定横纵坐标轴的坐标范围 
#### pyplot的绘图区域
`plt.subplot(nrows,ncols,plot_number)`
* nrows:分割横轴数量
* ncols:分割纵轴数量 
* plot_numbers:当前绘图区所处位置数 

逗号可以省略 

#### pyplot的plot()函数 
`plt.plot(x,y,format_string,**kwargs)`
* x:x轴数据，列表或数组，可选
* y:y轴数据，列表或数组
* format_string: 控制曲线的格式字符串，可选
   > 由颜色字符、风格字符、标记字符组成

   |颜色字符|说明|颜色字符|说明|
   |--|--|--|--|
   |'b'|蓝色|'m'|洋红色 magenta|
   |'g'|绿色|'y'|黄色|
   |'r'|红色|'k'|黑色|
   |'c'|青绿色cyan|'w'|白色|
   |'#008000'|RGB某颜色|'0.8'|灰度值字符串|

   |风格字符|说明|
   |--|--|
   |'-'|实线|
   |'--'|破折线|
   |'-.'|点化线|
   |':'|虚线|
   |''|无线条| 

   |标记字符|说明|
   |--|--|
   |'.'|点标记|
   |','|像素标记（极小点）|
   |'o'|实心圈标记|
   |'v'|倒三角标记|
   |'^'|上三角标记|
   |'>'|右三角|
   |'<'|左三角|
* **kwargs: 第二组或更多(x,y,format_string) 
  1. color:控制颜色 color='green'
  2. linestyle:线条风格  linestyle='dashed'
  3. marker:标记风格 marker='o'
  4. markerfacecolor:标记颜色 markerfacecolor='blue'
  5. markersize:标记尺寸 markersize=20

当绘制多条曲线时，各条曲线的x不能省略 
#### pyplot的中文显示
* 第一种方法:
pyplot并不默认支持中文显示，需要rcParams修改字体实现
改变全局字体的资源库 
``` python 
import matplotlib 
matplotlib.rcParams['font.family'] = 'SimHei'
```
rcParams的属性
|属性|说明|
|--|--|
|'font.family'|用于显示字体的名字|
|'font.style'|字体风格，正常'normal'或斜体'italic'|
|'font.size'|字体大小，整数字号或者'large'、'x-small'| 

中文字体:'SimHei':中文黑体 'Kaiti':中文楷体 'LiSu':中文隶书  
         'FangSong'：中文仿宋 'YouYuan':中文幼圆 'STSong':华文宋体 

* 第二种方法： 
在有中文输出的地方，增加一个属性：fontproperties 

#### pyplot的文本显示函数
|函数|说明|
|--|--|
|plt.xlabel()|对X轴增加文本标签|
|plt.ylabel()|对Y轴增加文本标签|
|plt.title()|对图形整体增加文本标签|
|plt.text()|在任意位置增加文本|
|plt.annotate()|在图形中增加带箭头的注解| 

plt.annotate(s,xy=arrow_crd,xytext=text_crd,arrowprops=dict)
* s:要注解的字符串
* xy:箭头所在的坐标位置
* xytext:箭头文本所在的坐标位置
* arrowprops:定义了箭头的属性  
``` python 
plt.annotate('注解',xy=(2,1),xytext=(3,4),
            arrowprops=(facecolor='black',shrink=0.1,width=2))

#facecolor:箭头颜色
#shrink:箭头两侧的缩进
#width:箭头的宽度
``` 

#### pyplot的子绘图区域
plt.subplot2grid() 

plt.subplot2grid(GridSpec,CurSpec,colspan=1,rowspan=1) 

理念：设定网格，选中网格，确定选中行列区域数量，编号从0开始 
* GridSpec:元组类型，画布切分网格数 
* CurSpec:元组类型，子图起始位置 
* colspan:横轴延伸覆盖结束位置
* rowspan:纵轴延伸覆盖结束位置  

GridSpec类 
``` python 
import matplotlib.gridspec as gridspec 

gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,-1])
ax3 = plt.subplot(gs[1:,-1])
```
#### pyplot的基础图表函数 
|函数|说明|
|--|--|
|plt.plot(x,y,fmt,...)|绘制一个坐标图|
|plt.boxplot(data,notch,postition)|绘制一个箱形图|
|plt.bar(left,height,width,bottom)|绘制一个条形图|
|plt.bar(width,bottom,left,height)|绘制一个横向条形图|
|plt.polar(theta,r)|绘制极坐标图|
|plt.pie(data,explode)|绘制饼图|
|plt.psd(x,NFFT=256,pad_to,Fs)|绘制功率谱密度图|
|plt.speegram(x,NFFT=256,pdf_to,F)|绘制谱图|
|plt.cohere(x,y,NFFT=256,Fs)|绘制X-Y的相关性函数|
|plt.scatter(x,y)|绘制散点图，其中，x和y长度相同|
|plt.step(x,y,where)|绘制步阶图|
|plt.hist(x,bins,normer)|绘制直方图| 

####饼图的绘制