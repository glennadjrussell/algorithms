#!/usr/bin/env python

# O(n^2)
def bubblesort(arr):
	arrlen = len(arr)
	if arrlen > 1:
		while True:
			swapped = False
			for x in range(0, arrlen-1):
				if arr[x] > arr[x + 1]:
					swapval = arr[x]
					arr[x] = arr[x + 1]
					arr[x + 1] = swapval
					swapped = True

			if not swapped:
				break
	return arr

if __name__ == '__main__':
	print bubblesort([8, 5, 3, 4, 100, 1000, 101])

