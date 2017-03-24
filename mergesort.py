# O(n log n)
def merge(a, b):
	arr = []
	i = 0
	j = 0

	while len(a) > 0 and len(b) > 0:
		av = a[0]
		bv = b[0]

		if av > bv:
			del b[i]
			arr.append(bv)
		else:
			del a[i]
			arr.append(av)
	if len(a) > 0:
		arr.extend(a)

	if len(b) > 0:
		arr.extend(b)

	return arr

def mergesort(arr):
	arrlen = len(arr)
	if arrlen == 1:
		return arr
	else:
		mid = arrlen // 2
		left = arr[:mid]
		right = arr[mid:]

		return merge(mergesort(left), mergesort(right))

if __name__ == '__main__':
	print mergesort([10, 10, 10001, 4, 67, 3, 5, 1, 2, 7])
