#!/usr/bin/env python

def quicksort(arr):
	arrlen = len(arr)
	if arrlen > 1:
		pivot = arrlen // 2
		pivotval = arr[pivot]
		newarr = [pivotval]

#		lowSide = [x for x in arr if x < pivotval]
#		highSide = [x for x in arr if x > pivotval]

		x = 0
		count = 0
		while count < arrlen:
			if arr[x] > pivotval and x < pivot:
				mv_val = arr.pop(x)
				arr.insert(pivot+1, mv_val)
			elif arr[x] < pivotval and x > pivot:
				mv_val = arr.pop(x)
				arr.insert(pivot-1, mv_val)
				x = x + 1
			else:
				x = x + 1

			count = count + 1
	
	return arr

if __name__ == '__main__':
	testarr = [4, 5, 1, 6, 2, 9, 7, 3]
	print quicksort(testarr)
