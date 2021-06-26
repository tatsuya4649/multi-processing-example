#!/bin/env python

import time
import queue
from multiprocessing.managers import BaseManager

# Register Manager like Manager
BaseManager.register('get_task')
BaseManager.register('get_result')

_server_addr = '127.0.0.1'
print(f"Connect to server {_server_addr}...")

manager = BaseManager(address=(_server_addr,5000),authkey=b'tatsuya')
manager.connect()

# Get Queue
task = manager.get_task()
result = manager.get_result()

# Get Task from Server, and put result into Server
for i in range(10):
	try:
		n = task.get(timeout=1)
		print(f'run task {n}+{n}')
		r = n + n
		result.put(r)
	except queue.Empty:
		print('task queue is empty')

print('end Work')

