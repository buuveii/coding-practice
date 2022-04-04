def bubble_sort(arr):
    l = len(arr)

    for i in range(l):
        for j in range(0, l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [3, 8, 10, 1, 4, 5, 6]
print("Unsorted array is:")
print(arr)

bubble_sort(arr)

print("Sorted array is:")
print(arr)