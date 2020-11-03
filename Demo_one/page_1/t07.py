import time,threading

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
def thread_2():
    print('thread %s is running...' % threading.current_thread().name)
    for i in ['A','B','C']:
        print('thread %s >>> %s'% (threading.current_thread().name,i))
        time.sleep(1)
    print('therad %s is ended.'% threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t1 = threading.Thread(target=loop)
t2 = threading.Thread(target=thread_2)
t1.start()
t2.start()
t1.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)