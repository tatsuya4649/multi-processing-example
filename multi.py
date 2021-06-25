#!/bin/env python

import multiprocessing as multi
import os

def get_process(process_name):
	print(f"Process \"{process_name}\" => {os.getpid()}")

if __name__ == "__main__":
	get_process("now")
	# Start Another Process,Like threading
	p = multi.Process(target=get_process,args=("multi",))
	p.start()
	p.join()
