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
    tmp_max_idx = idx
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2
    if left_child < size and arr[left_child] > arr[tmp_max_idx]:
        tmp_max_idx = left_child
    if right_child < size and arr[right_child] > arr[tmp_max_idx]:
        tmp_max_idx = right_child
    # # Check if it needs to swap or not?
    if tmp_max_idx != idx:
        arr[idx], arr[tmp_max_idx] = arr[tmp_max_idx], arr[idx]
        heapify(arr, size, tmp_max_idx)


def heapSort(arr):
    size = len(arr)

    # # Construct max heap
    for i in range(size // 2 - 1, -1, -1):
        # # Debugging.
        print('Debugging:', i)
        heapify(arr, size, i)
        print('Debugging:', arr)
    # # Debugging.
    # print('Debugging:', arr)

    # Swap the root(idx = 0) to the end of the array.
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # # Heapify root element
        heapify(arr, i, 0)


if __name__ == '__main__':
    print('Default: ', data)
    heapSort(data)
    print('Sorted: ', data)
