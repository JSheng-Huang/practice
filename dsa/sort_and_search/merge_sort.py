"""Merge Sort
Refer to: https://hackmd.io/@coherent17/Sy79MIyju
Created by JSheng <jasonhuang0124@gmail.com>"""


def mergeSort(arr):
    """mergeSort()
    Find the division point.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)

        """Initialize the comparison indices."""
        right_idx = 0
        left_idx = 0
        merge_idx = 0

        """Case 1: The left array compares with the right array."""
        while len(left_arr) > left_idx and len(right_arr) > right_idx:
            if left_arr[left_idx] > right_arr[right_idx]:
                arr[merge_idx] = right_arr[right_idx]
                right_idx += 1
            else:
                arr[merge_idx] = left_arr[left_idx]
                left_idx += 1
            merge_idx += 1
        """
        Case 2 & 3 are designed while one of two pointers has reached the end."""
        """Case 2: The left array compares with itself."""
        while len(left_arr) > left_idx:
            arr[merge_idx] = left_arr[left_idx]
            left_idx += 1
            merge_idx += 1
        """Case 3: The right array compares with itself."""
        while len(right_arr) > right_idx:
            arr[merge_idx] = right_arr[right_idx]
            right_idx += 1
            merge_idx += 1
    return arr


if __name__ == '__main__':
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    # data = [10, 80, 70, 20, 30, 90, 40]
    print('Default: ', data)
    mergeSort(data)
    print('Sorted: ', data)
