### Series类型 
series 类型是由一组数据及与之相关的数据索引组成
一维带标签的数组
（1）自动索引 （2）自定义索引  
> 自动索引和自定义索引并存,但不能混用

索引作为第二个参数，可以省略index=
#### Series 类型可以由以下类型创建
* python列表 
* 标量值  由标量值创建的时候，必须要指定`index`
``` python 
s = pd.Series(25,index=['a','b','c'])
```
* python字典 
``` python
s = pd.Series({'a':1,'b':2,'c':3})
```
* ndarray  
``` python 
pd.Series(np.arange(5))  
```
* 其他函数： range()函数 
####　Series类型基本操作  
* s.index  获得索引 Index类型
* s.values 获得数据 Ndarray类型 
* 索引采用[]
* Numpy中运算和操作可用于Series类型
* 可以通过自定义索引的列表进行切片
#### Series类型对齐操作 （基于索引）
Series + Series 
``` python
import pandas as pd 
a = pd.Series([1,2,3],['c','d','e'])
b = pd.Series([1,2,3,4],['a','b','c','d']) 
```
> Series 类型在运算中会自动对齐不同索引的数据
####　Series类型的name属性 
Series对象和索引都可以有一个名字，存储在属性.name中 
```python 
import pandas as pd 
b = pd.Series([9,8,7,6],index=['a','b','c','d'])
b.name = 'Series对象'
b.index.name = '索引列'
``` 

### DataFrame类型
DataFrame类型由共用相同索引的一组列组成
```
index_0 --> data_a   data_1    data_w
index_1 --> data_b   data_2    data_x
index_2 --> data_c   data_3    data_y
index_3 --> data_d   data_4    data_z
```
* 列索引：纵向的为index   轴axis = 0 
* 行索引：横向的为column  轴axis = 1 
#### DataFrame类型可以由如下类型创建
* 二维ndarray对象
``` python 
import numpy as np 
import pandas as pd 
df = pd.DataFrame(np.arange(10).reshpae(2,5))
```
* 由一维Ndarray、列表、字典、元组和Series构成的字典
``` python 
dt = {'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([6,7,8,9],index=['a','b','c','d'])}
df = pd.DataFrame(dt)
#使用列表类型字典创建
dl = {'one':[1,2,3,4],
      'two':[9,8,7,6]}
d = pd.DataFrame(df,index=['a','b','c','d'])
```
* Series类型
* 其他DataFrame 

### Pandas库的数据类型操作 
如何改变Series和DataFrame对象（指的是增加、重排、删除索引）
#### 增加或重排：重新索引 
* 重新索引 
> .reindex()能够改变或重排Series和DataFrame索引

.reindex(index=None,columns=None,...)的参数
|参数|说明|
|--|--|
|index, columns|新的行列自定义索引|
|fill_value|重新索引中，用于填充缺失位置的值|
|method|填充方法，ffill当前值向前填充,bfill向后填充|
|limit|最大填充量|
|copy|默认为True,生成新的对象，False时，新旧相等不复制| 
---
Series 和 DataFrame的索引是Index类型
Index对象是不可修改类型
* 索引类型的常用方法:

|方法|说明|
|--|--|
|.append(idx)|连接另一个index对象，产生新的Index对象|
|.diff(idx)|计算差集，产生新的index对象|
|.intersection(idx)|计算交集|
|.union(idx)|计算并集|
|.delete(loc)|删除loc位置出的元素|
|.insert(loc,e)|在loc位置处增加一个元素e|

#### 删除：drop方法
.drop()能够删除Series和DataFrame指定行或列索引
如果要删除列，要指定axis=1,默认删除0轴元素

### Pandas库的数据类型运算
算数运算法则：
* 算数运算根据行列索引，补齐后运算，运算默认产生浮点数
* 补齐时缺项填充NaN（空值）
* 二维和一维、一维和零维间 为广播运算
* 采用+-*/符号进行的二元运算产生新的对象 
#### 数学类型的算数运算 方法形式的运算 
|方法|说明|
|--|--|
|.add(d,*argws)|类型间加法运算，可选参数|
|.sub(d,*argws)|类型间减法运算，可选参数|
|.mul(d,*argws)|类型间乘法运算，可选参数|
|.div(d,*argws)|类型间除法运算，可选参数| 
`a.add(b,fill_value=100)` 
不同维度间为广播运算，一维Series默认在轴1参与运算
----
比较运算法则：
* 比较运算只能比较相同索引的元素，不进行补齐
* 二维和一维、一维和零维间 为广播运算
* 采用> < <= >= != ==等符号进行的二元运算产生布尔对象
> 同维度运算，要求尺寸一致
> 不同维度，广播运算，默认在1轴 


### 数据排序
* .sort_index()方法在指定轴上根据**索引**进行排序，默认升序

`.sort_index(axis=0,ascending=True)`
* .sort_index()方法在指定轴上根据**数值**进行排序，默认升序 

`Seriese.sort_values(axis=0,ascending=True)`
`DataFrame.sort_values()` 

### 数据的清洗
* `df.columns = ['a','b'] #重命名数据框的列名称`
* `df.isnull() #检查数据中空值出现的情况，并反馈一个由布尔值组成的列 `
* `df.notnull() #检查数据中非空值出现的情况，并反馈一个由布尔值组成的列 `
* `df.dropna() #移除数据框DataFrame中包含空值的行` 
* `df.dropna(axis=1) #移除数据框DataFrame中包含空值的列`  
* `df.fillna(x) #将数据框DataFrame中的空值全部替换为x`
* `s.astype(float) #将数组Series的格式转换为浮点数`
* `s.replace(1,'one') #将数组Series中的1全部替换为one`

### 数据的过滤（filter）、排序(sort)和分组(groupby) 
* `df[df['A']>0.5] #选取DataFrame中对应行的数值大于0.5的全部列`
* `df.sort_values(col1) #将DataFrame按照col1列数值的升序进行排列`
* `df.sort_values(col1,ascending=False) #将DataFrame按照col1列数值的降序进行排列`
* `df.sort_values([col1,col2],ascending=[True,False]) #将DataFrame按照col1列升序\col2降序进行排列`
* `df.groupby(col) #按照某列对数据df进行分组`
* `df.groupby([col1,col2]) #按照col1,col2对数据df进行分组` 
* `df.groupby(col1) #按照某列对数据df进行分组`
* `df.groupby(col1)[col2].mean() #按照col1列进行分组，返回col2的平均值`
* `df.apply(np.mean) #对df的每一列求平均值` 
* `df.apply(np.max,axis=1) #对df的每一行求最大值` 

### 数据的连接与整合
* `df.append(df2) #在df2的末尾添加df1，相当于union all`
* `pd.concat([df1,df2],axis=1) #axis=1时，df1横向末尾添加df2，axis=0时，df1纵向末尾添加df2`
* `df1.join(df2,on=col,how='inner') #对数据df1和df2进行内连接，连接的列为col`

### 数据的统计
* `df.describe() #得到df每一列的描述性统计`
* `df.mean() #得到每一列的平均值`
* `df.corr() #得到每一列与其他列的相关系数`
* `df.count() #得到每一列非空值的个数`
* `df.max() #得到每一列的最大值`
* `df.min() #得到每一列的最小值`
* `df.median() #得到每一列的中位数`
* `df.std() # 得到每一列的标准差`





