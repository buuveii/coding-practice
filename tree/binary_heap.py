from heapq import heapify, heappush, heappop

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    def insertKey(self, key):
        heappush(self.heap, key)

    def extractMin(self):
        return heappop(self.heap)

    def getMin(self):
        return self.heap[0]

def min_heapify(list):
        return heapify(list)

def main():
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
    list = [3, 9, 8, 1, 3, 5]
  
    print(heapObj.extractMin())
    print(heapObj.getMin())
    print(heapObj.heap)
    min_heapify(list)
    print(list)

if __name__ == '__main__':
    main()