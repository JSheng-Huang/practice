"""Longest Increasing Subsequence
Problem:
    Given an array `arr[]` of size `n`, the task is to find the length of the
longest increasing subsequence i.e., the longest possible subsequence in 
which the elements of the subsequence are sorted in increasing order.
Refer to:
    1. https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
    Time Complexity: O(n^2), where `n` is the size of array.
    Space Complexity: O(n), use of any array to store the longest increasing subsequence values at each index.
Created by JSheng <jasonhuang0124@gmail.com>"""


def longestIncreasingSubsequence(arr):
    arr_len = len(arr)

    """Store the longest increasing subsequence values at each index."""
    lis = [1] * arr_len

    for i in range(1, arr_len):
        for j in range(0, i):
            """
            `lis[j]` equals to that if `arr[j]` is considered as the end in the 
            longest increasing subsequence when the idx is `j`, and the length 
            of it would be. So if `arr = [10, 22, 9]`, and `arr[2] = 1` because 
            `9` is smaller than both `10` and `22`, if it is taken as the end 
            in the longest increasing subsequence, the longest increasing 
            subsequence is `[9]`.
            """
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    ans = max(lis)
    return ans


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of the longest increasing subsequence is",
          longestIncreasingSubsequence(arr))
