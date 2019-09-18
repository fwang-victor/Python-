import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path = 'D:/personal_data/python_code/PythonCode/Data/human_one/HR_comma_sep.csv'
df = pd.read_csv(path)
null_cnt = df.isnull().sum()
print(df.iloc[:5,2:5])
print(null_cnt)
print(df.columns)
df = df.rename(columns={"sales":"department",
                        "promotion_last_5years":"promotion",
                        "Work_accident":"work_accident"})
print(df.shape)
print(df.describe(include='O'))
#print(df['department'])
#print(df['salary'])
df['department'] = df['department'].astype('category')
df['salary'] = df['salary'].astype('category')

#salary_dict = dict(enumerate(df['salary'].cat.categories))
#department_dict = dict(enumerate(df['department'].cat.categories))
#print(salary_dict,department_dict)

for feature in df.columns:
    if str(df[feature].dtype) == 'category':
        df[feature] = df[feature].cat.codes
        df[feature] = df[feature].astype('int64')

#print(df['left'].value_counts())

left_mean = df.groupby('left').mean()
#print(left_mean)

work_accident = df['work_accident'].value_counts()
on_job = work_accident[0]
leave_job = work_accident[1]
#print(on_job,leave_job)
rate = [round(on_job/(on_job+leave_job) * 100,2),
        round(leave_job/(on_job+leave_job) * 100,2)]
explode = [0.2,0]
labels = ['on','leave']

'''
plt.pie(rate,
        explode=explode,
        labels=labels,
        autopct='%.2f%%')
plt.show()
 '''
'''
satisfaction_mean = df.groupby('time_spend_company')['satisfaction_level'].mean()
print(satisfaction_mean)

plt.bar(satisfaction_mean.index,
        satisfaction_mean.values,
        align='center')
plt.xlabel('time_spend_company')
plt.ylabel('satisfaction_level')
for x,y in zip(satisfaction_mean.index,satisfaction_mean.values):
    plt.text(x,y+0.01,round(y,2),ha='center')
plt.show()
'''
print(df['department'].unique())
salary_cnt = df.groupby(['department','salary'])['promotion'].count()
print(salary_cnt)
left_cnt = df.groupby(['department','left'])['promotion'].count()
print(left_cnt)