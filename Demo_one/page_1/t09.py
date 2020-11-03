import threading
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))

def process_thread(name:str):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=("Peter",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("Raymond",),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#如果需要在线程中使用到局部变量，可以使用local来保存
#可以将threading.local看成一个字典: key = 进程名 value = 局部变量