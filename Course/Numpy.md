### 数据的维度
一维数据由对等关系的有序或无序数据构成，采用线性方式组织
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

