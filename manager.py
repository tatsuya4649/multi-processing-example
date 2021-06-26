#!/bin/env python

import multiprocessing as multi

def dict_add(dict,i):
	dict[i] = True
def list_add(list,i):
	list.append(i)

with multi.Manager() as manager:
	shared_dict = manager.dict()
	shared_list = manager.list()
	p_list = []
	for i in range(100):
		p1 = multi.Process(target=dict_add,args=(shared_dict,i,))
		p2 = multi.Process(target=list_add,args=(shared_list,i,))
		p1.start()
		p2.start()
		p1.join()
		p2.join()
	print(shared_dict)
	print(shared_list)
