import pandas as pd 
import numpy  as np 
from matplotlib import pyplot as plt 


def Person_Statistic():
    '''按人员统计工作量'''
    #
    person=('a','b','c','d')
    workload=(760,740,720,730)
    #
    plt.figure('statistic_figure',figsize=(8,6),dpi=100)
    plt.title('person_statistic')
    #
    index=np.arange(len(person))
    bar_width=0.35
    #
    plt.bar(index,workload,width=bar_width,color='b')
    for x,y in zip(index,workload):
        plt.text(x+bar_width/2,y+0.2,y,ha='center',va='bottom')

    plt.xticks(index+bar_width/2,person)

    plt.show()
    return 

Person_Statistic() 



