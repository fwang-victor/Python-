#导入库
import re
import numpy as np
from  sklearn import linear_model
from matplotlib import pyplot as plt

#导入数据
with open('D:/personal_data/python_book/chapter1/data.txt','r') as file:
    all_data = file.readlines()

    #print(all_data)

#数据预处理
x = []
y = []
for single_data in all_data:
    tmp_data = re.split('\t|\n',single_data)
    x.append(float(tmp_data[0]))
    y.append(float(tmp_data[1]))

x = np.array(x).reshape(100,1)
y = np.array(y).reshape(100,1)

#数据分析
plt.scatter(x,y)
plt.show()

#数据建模
model = linear_model.LinearRegression()
model.fit(x,y)

#模型评估
model_coef = model.coef_
model_interpect = model.intercept_
r2 = model.score(x,y)

#销售预测
new_x = 84610
pre_y = model.predict(new_x)
print(pre_y)
