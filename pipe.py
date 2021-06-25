#!/bin/env python
import multiprocessing as multi


def pwrite(conn):
	conn.send(1)
	conn.close()

def cread(conn):
	print(conn.recv())
	conn.close()

if __name__ == "__main__":
	pp,cp = multi.Pipe()
	p = multi.Process(target=cread,args=(cp,))
	c = multi.Process(target=pwrite,args=(pp,))
	p.start()
	c.start()
	p.join()
	c.join()
