"""Heap
Refer to:
    1. https://www.shubo.io/binary-heap/
Created by JSheng <jasonhuang0124@gmail.com>"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Append the new value in the tail."""
        self.heap.append(value)

        """
        Keep comparing the new value until it is less or equal to its parent.
        """
        self.compare_to_root()

    def compare_to_root(self):
        idx = len(self.heap) - 1
        while idx > 0 and self.heap[(idx - 1) // 2] < self.heap[idx]:
            self.heap[(idx - 1) //
                      2], self.heap[idx] = self.heap[idx], self.heap[(idx - 1) // 2]
            idx = (idx - 1) // 2

    def extract_max(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        """
        Keep comparing the new root value which was in the tail until it is
        larger or equal to its children.
        """
        self.compare_to_bottom()

        return value

    def compare_to_bottom(self):
        root_idx = 0
        while (len(self.heap) > root_idx * 2 + 1):
            next_idx = root_idx * 2 + 1
            if len(self.heap) > root_idx * 2 + 2 and self.heap[root_idx * 2 + 2] > self.heap[root_idx * 2 + 1]:
                next_idx = root_idx * 2 + 2
            if self.heap[root_idx] < self.heap[next_idx]:
                self.heap[root_idx], self.heap[next_idx] = self.heap[next_idx], self.heap[root_idx]
                root_idx = next_idx
            # # Set an early breakpoint to improve T(n).
            else:
                break


heap_arr = MaxHeap()
heap_arr.insert(3)
heap_arr.insert(9)
heap_arr.insert(2)
heap_arr.insert(1)
heap_arr.insert(4)
heap_arr.insert(5)
print(heap_arr.heap)
