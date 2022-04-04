def insertionSort(arr):
    l = len(arr)

    for i in range(1, l):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

arr = [3, 8, 4, 12, 34, 54, 1]
print("Unsorted array is:")
print(arr)

insertionSort(arr)

print("Sorted array is:")
print(arr)
