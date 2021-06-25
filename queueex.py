#!/bin/env python

import multiprocessing as multi
import os
import time


def put():
	global q
	q.put(1)
	print("put")
def get():
	global q
	q.get(True)
	print("get")

if __name__ == "__main__":
	q = multi.Queue()
	p1 = multi.Process(target=get)
	p2 = multi.Process(target=put)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
