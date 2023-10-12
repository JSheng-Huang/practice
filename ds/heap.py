# Refer to: https://www.shubo.io/binary-heap/
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.__swim(len(self.heap) - 1)

    def extract_max(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__sink(0)
        return value

    def __swim(self, k):
        while (k > 0 and self.heap[(k - 1) // 2] < self.heap[k]):
            self.__swap((k - 1) // 2, k)
            k = (k - 1) // 2

    def __sink(self, k):
        while (k * 2 + 1 < len(self.heap)):
            j = k * 2 + 1
            if (k * 2 + 2 < len(self.heap) and self.heap[k * 2 + 2] > self.heap[k * 2 + 1]):
                j = k * 2 + 2

            if (self.heap[j] > self.heap[k]):
                self.__swap(j, k)

            k = j

    def __swap(self, j, k):
        tmp = self.heap[j]
        self.heap[j] = self.heap[k]
        self.heap[k] = tmp


heap_arr = MaxHeap()
heap_arr.insert(3)
heap_arr.insert(9)
heap_arr.insert(2)
heap_arr.insert(1)
heap_arr.insert(4)
heap_arr.insert(5)
print(heap_arr.heap)
