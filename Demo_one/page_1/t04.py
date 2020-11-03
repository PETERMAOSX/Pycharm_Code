from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print("Run task %s (%s)..."% (name,os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print("Task %s runs %0.2f seconds." %(name,(end - start)))

print("Parent process %s." % os.getpid())
p = Pool(8)  #设置成8 就是同时跑八个进程
for i in range(8):
    p.apply_async(long_time_task,args=(i,))
print('waiting for all subprocesses done...')
p.close()
p.join()
print("done......")