class MinHeap:
    def __init__(self):
        #self.cur_size = -1
        self.heap = []

    def parent(self, i):
        return int((i-1)/2)

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def insertKey(self, key):
        
        self.heap.append(key)
        #self.cur_size += 1
        
        current = len(self.heap) - 1

        while self.heap[current] < self.heap[self.parent(current)]:
            self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
            current = self.parent(current)

    def isLeaf(self, i):
        return self.left_child(i) > len(self.heap) - 1

    def min_heapify(self, i):
        if not self.isLeaf(i):
            if self.right_child(i) > len(self.heap) - 1: #baruun children bhgu bol
                if self.heap[i] > self.heap[self.left_child(i)]:
                    self.heap[i], self.heap[self.left_child(i)] = self.heap[self.left_child(i)], self.heap[i]

            else:
                if self.heap[i] > self.heap[self.left_child(i)] or self.heap[i] > self.heap[self.right_child(i)]:

                    if self.heap[self.left_child(i)] < self.heap[self.right_child(i)]:
                        self.heap[i], self.heap[self.left_child(i)] = self.heap[self.left_child(i)], self.heap[i]
                        self.min_heapify(self.left_child(i))
                
                    else:
                        self.heap[i], self.heap[self.right_child(i)] = self.heap[self.right_child(i)], self.heap[i]
                        self.min_heapify(self.right_child(i))

    def build_minHeap(self):
        for i in range(self.parent(len(self.heap)-1), 0, -1):
            self.min_heapify(i)

    def extractMin(self):
        self.heap[0] = self.heap[len(self.heap) - 1]
        #self.cur_size -= 1
        self.min_heapify(0)
        self.heap = self.heap[:len(self.heap) - 1]
        
    def getMin(self):
        return self.heap[0]


def main():
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
    heapObj.build_minHeap()
    
    print(heapObj.getMin())
    print(heapObj.heap)
    heapObj.extractMin()
    print(heapObj.heap)

if __name__ == '__main__':
    main()