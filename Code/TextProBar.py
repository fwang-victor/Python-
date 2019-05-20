import time 

scale = 50
print('执行开始'.center(20,'-'))
start_time = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '-'*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start_time
    print('\r{:3.0f}%[{}->{}]{:.2f}'.format(c,a,b,dur),end='')
    time.sleep(0.1)

print('\n'+'执行结束'.center(20,'-'))