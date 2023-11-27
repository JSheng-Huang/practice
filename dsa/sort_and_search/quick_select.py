"""Quick Select
Refer to:
    #1. https://magiclen.org/quickselect/ 
        #1.1 The manipulation is right, but the example is wrong.
    #2. https://www.geeksforgeeks.org/quickselect-algorithm/
Assumption: All elements in `arr[]` are distinct.
Created by JSheng <jasonhuang0124@gmail.com>"""


def partition(arr, left_idx, right_idx):
    """partition()
    It considers the last element as pivot and moves all smaller element to 
    left of it and greater elements to right.
    """
    pivot = arr[right_idx]
    idx = left_idx
    for i in range(left_idx, right_idx):
        if arr[i] <= pivot:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    """Swap the pivot to the right position."""
    arr[idx], arr[right_idx] = arr[right_idx], arr[idx]

    return idx


def kthSmallest(arr, left_idx, right_idx, k):
    """If k is smaller than number of elements in array."""
    if (k > 0 and k <= right_idx - left_idx + 1):
        """
        Partition the array around last element and get position of pivot 
        element in sorted array.
        """
        pivot_idx = partition(arr, left_idx, right_idx)

        """If position is same as input `k.`"""
        if (pivot_idx - left_idx == k - 1):
            return arr[pivot_idx]
        """If position is more, recur for left subarray."""
        if (pivot_idx - left_idx > k - 1):
            return kthSmallest(arr, left_idx, pivot_idx - 1, k)
        """
        Else recur for right subarray. `+ left_idx` needs to think for a while.
        """
        return kthSmallest(arr, pivot_idx + 1, right_idx,
                           k - pivot_idx + left_idx - 1)
    print('[ERROR] Index out of bound!')


arr = [47, 32, 30, 100, 38, 9, 101, 2, 61, 69, 81, 79]
n = len(arr)
k = 3
print('K-th smallest element is ')
print(kthSmallest(arr, 0, n - 1, k))
