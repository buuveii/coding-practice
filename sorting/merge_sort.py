def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        R = arr[r:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()


def main():
    arr = [3, 1, 6, 12, 865, 34, 2, 5]
    print("Unsorted array is:")
    print(arr)

    mergeSort(arr)

    print("Sorted array is:")
    printList(arr)

if __name__ == '__main__':
    main()  
