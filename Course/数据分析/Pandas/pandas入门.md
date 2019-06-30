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
* ndarray  
``` python 
pd.Series(np.arange(5))  
```
* 其他函数： range()函数 
####　Series类型基本操作  
* s.index  获得索引 index类型
* s.values 获得数据 ndarray类型 
* 索引采用[]
* Numpy中运算和操作可用于Series类型
* 可以通过自定义索引的列表进行切片
#### Series类型对齐操作 （基于索引）
Series + Series 
``` python
import pandas as pd 
a = pd.Series([1,2,3],['c','d','e'])
b = pd.Series([1,2,3],['a','b','c','d']) 
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
