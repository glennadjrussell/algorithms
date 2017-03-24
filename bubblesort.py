#!/usr/bin/env python

def bubblesort(arr):
	arrlen = len(arr)
	if arrlen > 1:
	swapped = False
	while True:
		i = 0
		for x in range(0, arrlen-1):
			if arr[x] > arr[x + 1]:
				swapval = arr[x]
				arr[x] = arr[x + 1]
				arr[x + 1] = swapval
				swapped = True
		if not swapped break
		
