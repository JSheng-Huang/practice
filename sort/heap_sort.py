# Refer to:
# https://hackmd.io/@coherent17/Sy79MIyju
# https://seanleetech.com/en/algorithm/168/
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

# data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]
data = [3, 9, 2, 1, 4, 5]


def heapify(arr, size, idx):
    root_idx = idx
    left_child_idx = 2 * idx + 1
    right_child_idx = 2 * idx + 2
    if left_child_idx < size and arr[left_child_idx] > arr[root_idx]:
        root_idx = left_child_idx
    if right_child_idx < size and arr[right_child_idx] > arr[root_idx]:
        root_idx = right_child_idx
    # # Check if it needs to swap or not?
    if root_idx != idx:
        # # Debugging.
        # print('===')
        # print(idx)
        # print(arr)
        arr[idx], arr[root_idx] = arr[root_idx], arr[idx]
        # print(arr)

        # # Validate that the swapping would have an impact on subtrees.
        heapify(arr, size, root_idx)


def heapSort(arr):
    size = len(arr)

    # # Construct a array which is max heap.
    for i in range(size // 2 - 1, -1, -1):
        # # Debugging.
        # print('Debugging:', i)
        heapify(arr, size, i)
        # print('Debugging:', arr)
    # # Debugging.
    # print('---')
    print('Debugging:', arr)

    # Swap the root(idx = 0) to the end of the subarray.
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # # Heapify once again to move the maximum to `arr[i]` for next
        # # swapping.
        heapify(arr, i, 0)


if __name__ == '__main__':
    print('Default: ', data)
    heapSort(data)
    print('Sorted: ', data)
