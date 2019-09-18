import re
from dateutil import rrule
from dateutil import parser
def count():
    str_input=input('请输入一个字符串:\n')
    set_str=set(str_input)
    cnt_list=[]
    for i in set_str:
        cnt=str_input.count(i)
        cnt_list.append(cnt)

    dict_cnt= dict(zip(list(set_str),cnt_list))
    max_value=max(dict_cnt.values())
    for key,value in dict_cnt.items():
        if  value==max_value:
            max_key=key
            print(max_key,dict_cnt[max_key])
    print(dict_cnt)

def Report_Period(title):
    ''' 根据公告标题获取报告期'''
    pattern=re.compile(r'2\d{3}')
    year=pattern.search(title).group()
    if re.search(r'年半年度(报告|财务报表)',title):
        return str(year)+'0630'
    elif re.search(r'年年度(报告|财务报表)',title):
        return str(year)+'1231'
    elif re.search(r'年一季度(报告|财务报表)',title):
        return str(year)+'0331'
    elif re.serach(r'年三季度(报告|财务报表)',title):
        return str(year)+'0930'
    else:
        None

def Time_diff(type,date1,date2):
    if (date1=='') or (date2=='') :
        return None
    else:
        date1=parser.parse(date1)
        date2=parser.parse(date2)
        if type=='day':
            diff=date1-date2 
        elif type=='week':
             diff=rrule.rrule(rrule.WEEKLY,dtstart=date1,until=date2)
        elif type=='month':
            diff=rrule.rrule(rrule.MONTHLY,dtstart=date1,until=date2)

    return diff



if __name__=='__main__':
    #count()
    #print(Report_Period('2018-08-10-华北制药2018年半年度报告'))
    print(Time_diff('day','20170225','20160225'))
    print(Time_diff('week','2017-02-25','2016-01-01'))
    #print(Time_diff('month','2017-07-25','20160225'))
    r=rrule.rrule(rrule.MONTHLY,dtstart=parser.parse('20180820'),until=parser.parse('20170821')).count()
    print(r)
 