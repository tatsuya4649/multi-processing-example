#!/bin/env python
import multiprocessing as multi
import os
import time

def print_pid():
	time.sleep(3)
	print(f"Process ID => {os.getpid()}")

if __name__ == "__main__":
	_PROCESS_COUNT = 100
	pool = multi.Pool(_PROCESS_COUNT)
	for i in range(_PROCESS_COUNT):
		# apply_async => asynchronous process
		pool.apply_async(print_pid)
		# apply => wait for ending process
		#pool.apply(print_pid)
	# close => prevent futher tasks from running
	pool.close()
	pool.join()
