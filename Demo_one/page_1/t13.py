from multiprocessing.managers import BaseManager
import random
import time
import queue

BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

server_addr = '127.0.0.1'
manager = BaseManager(address=(server_addr,5000),authkey=b'abc')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    try:
        temp = task.get(timeout=1)
        ans = temp * 2
        print("%s *2 = %s" % (temp,ans))
        time.sleep(1)
        result.put(ans)
    except queue.Queue().empty():
        print("task is empty")
print("Test Done....")
