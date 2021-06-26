#!/bin/env python
from concurrent.futures import ProcessPoolExecutor

def hello():
	print("hello world")

if __name__ == "__main__":
	exec = ProcessPoolExecutor(max_workers=10)
	future = exec.submit(hello)
	while True:
		if (future.done()):
			break
	exec.shutdown()
