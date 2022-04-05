def heapify(arr, l, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < l and arr[largest] < arr[left_child]:
        largest = left_child

    if right_child < l and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, l, largest) 

def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

arr = [1, 12, 9, 5, 6, 10]
print(arr)
heapSort(arr)
print(arr)