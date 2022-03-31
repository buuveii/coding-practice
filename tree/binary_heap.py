class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.cur_size = 0

    def parent(self, i):
        return int((i-1)/2)

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def move_up(self, i):
        while self.parent(i) > 0:
            if self.heap[i] < self.heap[self.parent(i)]:
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

            i = self.parent(i)

    def insertKey(self, key):
        self.heap.append(key)
        self.cur_size += 1
        self.move_up(self.cur_size)

    #def extractMin(self):
        
    def getMin(self):
        return self.heap[0]

    #def min_heapify(self, i):

def main():
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
  
    #print(heapObj.extractMin())
    print(heapObj.getMin())
    print(heapObj.heap)

if __name__ == '__main__':
    main()