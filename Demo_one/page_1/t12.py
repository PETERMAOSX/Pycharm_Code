from multiprocessing.managers import BaseManager
import queue
import random

task_queue = queue.Queue()
result_queue = queue.Queue()

BaseManager.register('get_task_queue',callable=lambda: task_queue)
BaseManager.register('get_result_queue',callable=lambda: result_queue)

manager = BaseManager(address=('',5000),authkey=b'abc')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    temp = random.randint(0,10000)
    print("put task value is %s. " % temp)
    task.put(temp)
print("wait for another threading callback")

for i in range(10):
    r = result.get(timeout=10)
    print("result = %s" % r)
print("Test Done....")