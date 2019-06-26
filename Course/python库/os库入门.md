### OS库笔记 
#### os库之路径操作
os.path子库以path为入口，用于操作和处理文件路径 
``` python 
import os.path
``` 
``` python 
import os.path as op
```
路径操作函数
|函数|说明|
|--|--|
|os.path.abspath(path)|返回path在当前系统中的绝对路径|
|os.path.normpath(path)|归一化path的表示形式，统一采用\\分隔路径|
|os.path.relpath(path)|返回当前程序与文件之间的相对路径（relative path）|
|os.path.dirname(path)|返回path中的目录名称|
|os.path.basename(path)|返回path中最后的文件名称|
|os.path.join(path,*paths)|组合path与paths，返回一个路径字符串|
|os.path.exists(path)|判断path对应文件或目录是否存在，返回True或False|
|os.path.isfile(path)|判断path所对应的是否为文件，返回True或False|
|os.path.isdir(path)|判断path所对应的是否为目录，返回True或False| 

文件操作时间函数
|函数|说明|
|--|--|
|os.path.getatime(path)|返回path对应文件或目录上一次的访问时间|
|os.path.getmtime(path)|返回path对应文件或目录最近一次的修改时间|
|os.path.getctime(path)|返回path对应文件或目录的创建时间| 

|函数|说明|
|--|--|
|os.path.getsize(path)|返回path对应的文件大小，以字节为单位| 

#### os的进程管理
os.system(command)
* 执行程序或命令command
* 在windows系统中，返回值为cmd的调用返回信息

#### os库之环境参数
|函数|说明|
|--|--|
|os.chdir(path)|修改当前程序操作的路径|
|os.getcwd()|返回程序的当前路径|
|os.getlogin()|获取当前系统登录用户|
|os.cpu_count()|获得当前系统的cpu数量|