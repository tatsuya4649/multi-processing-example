#!/bin/env python
import os

def print_pid():
	print(f"This process id => {os.getpid()}")

pid = os.fork()
if pid == 0:
	# Child
	print_pid()
else:
	# Parent
	print_pid()
