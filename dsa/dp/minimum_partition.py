"""Minimum Partition
Problem:
        Given a set of non-negative integers, the task is to divide it into two 
    sets S1 and S2 such that the absolute difference between their sums is 
    minimum. 
        If there is a set S with n elements, then if we assume Subset1 has m 
    elements, Subset2 must have `n - m` elements and the value of abs(sum
    (Subset1) – sum(Subset2)) should be minimum.
Example:
    Input: arr[] = {1, 6, 11, 5} 
    Output: 1
    Explanation:
        Subset1 = {1, 5, 6}, sum of Subset1 = 12
        Subset2 = {11}, sum of Subset2 = 11    
Refer to: https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
Time Complexity: 
        O(n * sum), where `n` is the number of elements and `sum` is the sum of 
    all elements.
Space Complexity: O(sum).
Created by JSheng <jasonhuang0124@gmail.com>"""


def minDifference(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    """
    The half of sum of two subsets would be the closet one to the difference of two subsets.
    """
    half_sum = sum // 2 + 1

    dp = [False for _ in range(half_sum)]
    curr_dp = [False for _ in range(half_sum)]

    """Image that the subset is empty in the beginning."""
    dp[0] = True

    for i in range(n):
        for j in range(half_sum):
            """
            `dp[j] == True` means `j` is one possible output which is combine 
            from numbers in `arr[i]` and it's less than `half_sum`.
            """
            if dp[j] and j + arr[i] < half_sum:
                curr_dp[j + arr[i]] = True
        for j in range(half_sum):
            if (curr_dp[j]):
                dp[j] = True
            curr_dp[j] = False
    for i in range(half_sum - 1, 0, -1):
        if dp[i]:
            """
            Since `i` is possible to form the number which is the closet to 
            `half_sum`, then the complementary of it is `sum - i`, so the 
            minimum difference is sum - 2 * i.
            """
            return sum - 2 * i
    return sum


if __name__ == '__main__':
    arr = [1, 5, 5, 11, 16]
    # arr = [5, 5, 6, 6]
    # arr = [1, 1, 1, 1, 1, 1]
    # arr = [0, 5]
    n = len(arr)
    print("The Minimum difference of 2 sets is ", minDifference(arr, n))
