#!/bin/env python

import multiprocessing as multi
from multiprocessing.managers import BaseManager
import queue
import random

# Register Manager and Worker
task_queue = queue.Queue()
res_queue = queue.Queue()

BaseManager.register('get_task',callable=lambda: task_queue)
BaseManager.register('get_result',callable=lambda: res_queue)

# Start Server
manager = BaseManager(address=('',5000),authkey=b'tatsuya')
manager.start()


# Get Queue Object via Remote Connection
task = manager.get_task()
result = manager.get_result()

# Put task in 'task_queue'
print(task)
print(result)
for i in range(10):
	n = random.randint(0,10000)
	print(f'Put task {n}')
	task.put(n)

# Get task in 'res_queue'
for i in range(10):
	r = result.get(timeout=10)
	print(f'Get task result {r}')

# End manager process
manager.shutdown()

print('end Manager')
