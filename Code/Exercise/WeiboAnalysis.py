import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re

file = 'D:/personal_data/python_code/PythonCode/Data/data7857/weibo.csv'
data = pd.read_csv(file)
#print(data.columns)  #查看列名
#重命名column列名
data.columns = ['id','user_name','weibo_level','weibo_content','forward','comments', 'thumbs', 'time']
#print(data.shape) #查看数据结构
#print(data.info()) #查看数据信息

#name_count = data[['user_name','weibo_content']].apply( lambda x : len(np.unique(x)))  #user_name weibo_content
#print(name_count)
#去除user_name和weibo_content两列的重复值
df = data.drop_duplicates(['user_name','weibo_content']).copy() #复制一份数据，避免后续的链式赋值
#print(df.shape)
user_type = df['weibo_level'].value_counts()
print(user_type.values)
#print(df.iloc[:,4:].head(10))

#
df.loc[df.comments == '评论','comments'] = 0
df.loc[df.forward == '转发','forward'] = 0
df.loc[df.thumbs == '赞','thumbs'] = 0
print(df.iloc[:5,4:])

# 处理forward、comments、thumbs 列中的数据，单位转换
df[['forward','comments','thumbs']] = df[['forward','comments','thumbs']].astype('str') #将数值转换为字符串
df.forward = df.forward.apply(lambda x:float(x[:-1])*10000 if x[-1] == '万' else float(x))
df.comments = df.comments.apply(lambda x:float(x[:-1])*10000 if x[-1] == '万' else float(x))
df.thumbs = df.thumbs.apply(lambda x:float(x[:-1])*10000 if x[-1] == '万' else float(x))
print(df.iloc[:5,4:])

#剔除time列
df = df.drop('time',axis=1)
print(df.columns)

#处理weibo_content列数据，剔除话题引用，剔除周杰伦超华，剔除非中文内容
df.weibo_content = df.weibo_content.apply(lambda x: re.sub(r'#.*#','',x))
df.weibo_content = df.weibo_content.apply(lambda x: re.sub(r'周杰伦超话','',x))
df.weibo_content = df.weibo_content.apply(lambda x: re.sub(r'[^\u4e00-\u9fa5]','',x))
#print(df['weibo_content'].head(10))

#用户类型分布图
figure = plt.figure()
plt.bar(x = np.arange(5),height=user_type.values,align='center')
plt.xticks(np.arange(5),labels=user_type.index,fontproperties='Kaiti')
plt.xlabel('类型',fontproperties='SimHei')
plt.ylabel('数量',fontproperties='SimHei')
plt.title('用户类型分布图',fontproperties='SimHei')
plt.show()







