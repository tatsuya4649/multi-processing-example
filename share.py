#!/bin/env python

import multiprocessing as multi


def change_value(n):
	n.value = 10000.0001
def change_array(a):
	for i in range(len(a)):
		a[i] = a[i] * 100


if __name__ == "__main__":
	num = multi.Value('d',0.0)
	arr = multi.Array('i',range(10))

	print("--------")
	print("Before")
	print(num.value)
	print(arr[:])
	print("--------")

	pn = multi.Process(target=change_value,args=(num,))
	pa = multi.Process(target=change_array,args=(arr,))
	pn.start()
	pa.start()
	pn.join()
	pa.join()

	print("--------")
	print("After")
	print(num.value)
	print(arr[:])
	print("--------")

