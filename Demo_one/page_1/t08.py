import threading,time
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def ran_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=ran_thread,args=(5,))
t2 = threading.Thread(target=ran_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
import multiprocessing
print(multiprocessing.cpu_count())
#多进程中各变量相互独立，多线程中变量可以共用
#我们要保证balance的计算正确，就要给change_it()上上一把锁，使得只有一个线程可以执行这个方法
#其他线程不能够同时执行change_it(),只能等待，直到锁被释放以后才能够使用。
#由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁。
#threading.Lock()