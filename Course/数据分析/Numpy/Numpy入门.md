### 数据的维度
一维数据由对等关系的有序或无序数据构成，采用线性方式组织
数组对象可以去掉元素间运算所需的循环，使一维向量更像单个数据
#### N维数组对象：ndarray 
ndarray是一个多维数组对象，由两部分构成：
* 实际的数据
* 描述这些数据的元数据（数据维度，数据类型）
np.array()生成一个adarray数组 
np.array()输出成[]形式，元素由空格分割 
轴（axis）：保存数据的维度  秩（rank）：轴的数量 
#### ndarray对象的属性
|属性|说明|
|--|--|
|.ndim|秩，即轴的数量或维度的数量|
|.shape|ndarray对象的尺度，对于矩阵，n行m列|
|.size|ndarray对象元素的个数，相当于.shape中的n*m的值|
|.dtype|ndarry对象的元素类型|
|.itemsize|ndarray对象中每个元素的大小，以字节为单位|

### ndarray数组的创建和变换 
创建方法：
* 从python中的列表、元组等类型创建ndarray数组
* 使用numpy中函数创建ndarray数组，如：arange,ones,zeros等
* 从字节流（raw bytes）中创建ndarray数组
* 从文件中读取特定格式，创建ndarray数组

#### 从python中的列表、元组等类型创建ndarray数组:
> `x = np.array(list/tuple)`
 `x = np.array(list/tuple,dtype = np.float32)`
当np.array()不指定dtype时，numpy将根据数据情况关联一个dtype类型

#### 使用numpy中函数创建ndarray数组：
|函数|说明|
|--|--|
|np.arange()|类似range()函数，返回ndarray类型，元素从0到n-1|
|np.ones(shape)|根据shape生成一个全1数组，shape是元组类型|
|np.zeros(shape)|根据shape生成一个全1数组，shape是元组类型|
|np.full(shape，val)|根据shape生成一个数组，每个元素值都是val|
|np.eye(n)|创建一个正方的n*n矩阵，对角线为1，其余为0| 

|函数|说明|
|--|--|
|np.ones_like(a)|根据数据a的形状生成一个全1数组|
|np.zeros_like(a)|根据数组a的形状生成一个全0数组|
|np.full_like(a,val)|根据数组a的形状生成一个数组，每个元素值都是val|

|函数|说明|
|--|--|
|np.linspace()|根据起止数据等间距的填充数据，形成数组，endpoint最后一个是否出现|
|np.concatenate()|将两个或多个数组合并成一个新的数组|

#### ndarray数组的维度变换
|方法|说明|
|--|--|
|.reshape(shape)|不改变数组元素，返回一个shape形状的数组，原数组不变|
|.resize(shape)|与reshape()功能一致，但修改原数组|
|.swappaxes(ax1,ax2)|将数组n个维度中两个维度进行调换|
|.flatten()|对数组进行降维，返回折叠后的一维数组，原数组不变|

####  数组的索引和切片 
* 索引 获取数组中特定位置元素的过程 
* 切片 获取数组中元素子集的过程

多维数组的索引
* 每个维度一个索引值，使用逗号分隔
多维数组的切片
* 选取一个维度用 “:”
* 每个维度切片方法与一维数组相同
* 每个维度可以使用步长跳跃切片

#### ndarray数组的运算
1. 数组与标量之间的运算 
数组与标量之间的运算作用于数组的每一个元素 
2. numpy 一元函数，对Ndarray中的数据执行元素级运算的函数 
|函数|说明|
|--|--|
|np.abs(x) np.fabs(x)||
|||
|||
|||
||| 

#### 数据的csv文件存取 
####　随机数函数
|函数|说明|
|--|--|
|rand()||
|randn()||
|randint()||
|seed(s)||