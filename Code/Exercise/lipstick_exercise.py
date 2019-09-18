import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'

filename = 'D:/personal_data/python_code/PythonCode/Data/lipstick5429/lipstick.csv'
df = pd.read_csv(filename)

#print(df.head())
df = df.drop('image_src',axis=1) #删除某一列的数据，df.drop(index=None,colums=None,inplace=False)
print(df.head())
print(df.columns)# 重命名 df.rename()或者 df.columns = []
print(df.shape)
#print(df.info())
df = df.dropna()
#print(df.info())


df['price'] = df.price.apply(lambda x:re.search('[\d.]+',x).group(0)).astype('float')
df['deal'] = df.deal.apply(lambda x:re.search('[\d.]+',x).group(0)).astype('float')
df['title'] = df.title.apply(lambda x:re.sub('【.*】','',x))



location = df.location.str.split(' ',expand=True) #expand=True,将分列后的结果转换为DataFrame
location.columns = ['province','city']
df = df.drop('location',axis=1)
#print(df[['price','deal','title']])
#df = pd.merge(df,location,left_index=True,right_index=True)
df = df.join(location)

df = df.fillna(axis=1,method='ffill')
#print(df.columns)
print(df.price.dtype)
df['sale'] =round( (df['price'].astype('float').mul(df['deal'].astype('float')))/ 10000 ,2)
print(df.sale.dtype)


# 可视化分析
province_sale = df.groupby('province')['sale'].sum().sort_values(ascending=False)[0:20]
plt.figure(figsize=(8,8))
ax1 = plt.subplot2grid((3,2),(0,0),colspan=2)
ax1.set_title('各省份口红销量汇总')
ax1.set_xlabel('省份')
ax1.set_ylabel('销量')
ax1.bar(range(len(province_sale)),province_sale)


#
city_sale = df.groupby('city')['sale'].sum().sort_values(ascending=False)[0:20]
ax2 = plt.subplot2grid((3,2),(1,0),colspan=2)
ax2.set_title('各城市口红销量汇总')
ax2.set_xlabel('城市')
ax2.set_ylabel('销量')
ax2.bar(range(len(city_sale)),city_sale)

#
ax3 = plt.subplot2grid((3,2),(2,0),colspan=2)
ax3.scatter(range(len(city_sale)),city_sale,s=city_sale/100,c=range(len(city_sale)))
plt.show()
