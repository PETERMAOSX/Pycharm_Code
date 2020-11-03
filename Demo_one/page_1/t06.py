from multiprocessing import Process,Queue
import os,time,random

def write(q:Queue):
    print("Process to write: ",os.getpid())
    for value in ['A','B','C','D','E']:
        print('Put %s to queue....'% value)
        q.put(value)
        time.sleep(random.random())

def read(q:Queue):
    print("Process to read: ",os.getpid())
    while True:
        value = q.get()
        print("Get %s from queue." % value)
q = Queue()
pw = Process(target=write,args=(q,))
pr = Process(target=read,args=(q,))
pw.start()  #启动子进程pw
pr.start()  #启用子进程pr
pw.join()   #等待pw结束
pr.terminate() #强制结束pr