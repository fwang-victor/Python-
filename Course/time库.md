import time
#获取时间
'''
time() 获取当前时间戳，计算机内部时间值，浮点数
ctime() 获取当前时间并以易读方式返回
gmtime() 获取当前时间，表示为计算机可处理的时间格式
'''
print(time.time())
print(time.ctime())
print(time.gmtime())
#时间格式化
'''
strftime(tpl,ts) 
tpl 是格式化模板字符串，用来定义输出效果 
ts  是计算机内部时间类型变量
strptime(str,tpl)
str 是字符串形式的时间值
tpl 是格式化模板字符串，用来定义输出效果
'''
#程序计时应用 
'''
测量时间：perf_counter() 
start_time = time.perf_counter() 
end_time = time.perf_counter()
end_time - start_time
生产时间：sleep()
'''