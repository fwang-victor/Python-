#字符串处理函数
'''
len()
str()
hex()
oct()
chr() 将Unicode编码，返回其对应的字符 unicode:编码方式 
ord() 返回字符对应的Unicode编码

''' 
for i in range(12):
    print(chr(9800 + i),end=' ')
#字符串处理方法
#方法 特指<a>.<b>()风格中的函数<b>()
'''
(1)str.lower()或str.upper() 返回字符串的副本，字符串转换为全部小写/大写
(2)str.split(sep=None)      返回一个列表，由str根据Sep被分隔的部分组成
(3)str.count(sub)           返回子串sub在str中出现的次数
(4)str.replace(old,new)     返回字符串副本，将old子串全部替换为new字符
(5)str.center(width[,fillchar]) 字符串根据宽度width居中，填充字符fillchar可选
(6)str.strip(chars)         从str中去掉其左侧和右侧的chars字符，默认去掉空格
(7)str.join(iter)           在iter变量除最后元素外每个元素后面增加一个str
'''
#字符串类型的格式化
#字符串格式化使用.format()方法，用法如下：
#<模板字符串>.format(<逗号分隔的参数>)
#槽机制和.format()实现字符串格式化
'''
{<参数序号>:<格式控制标记>}
:<填充><对齐><宽度><,><.精度><类型>
对齐：< 左对齐 >右对齐  ^居中对齐
整数类型：b(二级制),c,d,o(八进制),x,X 浮点数类型:e(科学技术法),E,f,%(百分数)
'''
print('{0:=^20}'.format('PYTHON'))