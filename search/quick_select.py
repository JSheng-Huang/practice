# Refer to:
# https://magiclen.org/quickselect/ # # The manipulation is right, but the
# example is wrong.
# https://www.geeksforgeeks.org/quickselect-algorithm/
#
# ASSUMPTION: All elements in arr[] are distinct.
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

# # It considers the last element as pivot
# # and moves all smaller element to left of
# # it and greater elements to right.
def partition(arr, left_idx, right_idx):
    pivot = arr[right_idx]
    idx = left_idx

    # # Debugging.
    print('Into partitioning...')
    print('Current `pivot`:', pivot)
    print('Current `arr`:', arr)
    print('---')

    for i in range(left_idx, right_idx):
        if arr[i] <= pivot:
            # # Debugging.
            print('If `arr[i]` <= `pivot`:')
            print('The last index which is larger than `pivot`:', idx)
            print('Looping `i`:', i)

            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1

            # # Debugging.
            print('`arr` after swapping values between the last index which is larger than `pivot` and looping `i`:')
            print(arr)
            print('---')
    # # Debugging.
    print('`arr` after swapping values between `pivot` and the last index which is larger than `pivot`:')

    # # Swap the pivot to the right position.
    arr[idx], arr[right_idx] = arr[right_idx], arr[idx]

    # # Debugging.
    print(arr)
    print('===')

    return idx


def kth_smallest(arr, left_idx, right_idx, k):
    # # If k is smaller than number of
    # # elements in array.
    if (k > 0 and k <= right_idx - left_idx + 1):
        # # Partition the array around last
        # # element and get position of pivot
        # # element in sorted array.
        pivot_idx = partition(arr, left_idx, right_idx)

        # # If position is same as input `k.`
        if (pivot_idx - left_idx == k - 1):
            return arr[pivot_idx]
        # # If position is more, recur
        # # for left subarray.
        if (pivot_idx - left_idx > k - 1):
            return kth_smallest(arr, left_idx, pivot_idx - 1, k)
        # # Else recur for right subarray.
        # # ?????
        return kth_smallest(arr, pivot_idx + 1, right_idx,
                            k - pivot_idx + left_idx - 1)
    print('[ERROR] Index out of bound!')


arr = [47, 32, 30, 100, 38, 9, 101, 2, 61, 69, 81, 79]
n = len(arr)
k = 2
print("K-th smallest element is ")
print(kth_smallest(arr, 0, n - 1, k))
