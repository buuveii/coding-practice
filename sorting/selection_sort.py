def selectionSort(arr):
    l = len(arr)
    
    for i in range(l):
        min_idx = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [3, 8, 1, 7, 10, 23, 77]
print("Unsorted array is:")
print(arr)

selectionSort(arr)
print("Sorted array is:")
print(arr)

