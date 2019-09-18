import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import re

filename = 'lagou.csv'
fieldnames = ['companySize','companyLabelList','workYear','education','positionName','salary','companyShortName','companyFullName']
df = pd.read_csv(filename,names=fieldnames)
print(df.iloc[:5,3:])
print(df.info())
print(df.isnull().sum())
df['companySize'] = df.companySize.apply(lambda x:re.search(r'[\d-]+',x).group())
print(df.iloc[:5,:5])