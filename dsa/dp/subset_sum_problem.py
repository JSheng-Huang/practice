"""Subset Sum Problem
Problem:
        Given a set of non-negative integers and a value sum, the task is to 
    check if there is a subset of the given set whose sum is equal to the given 
    sum. 
Refer to:
    1. https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
    Time Complexity:  O(sum * n), where `n` is the size of the array.
    Space Complexity: O(sum), as the size of the 1-D array is `sum` + 1.
Created by JSheng <jasonhuang0124@gmail.com>"""


def isSubsetSum(nums, n, sum):
    prev = [False] * (sum + 1)
    for i in range(1, n + 1):
        curr = [False] * (sum + 1)

        """`curr[0]` means to add to the empty set."""
        curr[0] = True

        for j in range(1, sum + 1):
            """
            If:
            Else:
            """
            if nums[i - 1] > j:
                curr[j] = prev[j]
            else:
                print('i', i)
                print('j', j)
                print('prev[j]', prev[j])
                print('prev[j - nums[i - 1]', prev[j - nums[i - 1]])
                curr[j] = prev[j] or prev[j - nums[i - 1]]
                print('---')
        print(prev)
        print(curr)
        # Now curr becomes prev for (i+1)-th element
        prev = curr
        print('===')
    return prev[sum]


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    sum_value = 6
    n = len(nums)
    if isSubsetSum(nums, n, sum_value):
        print("Found a subset with the given sum")
    else:
        print("No subset with the given sum")
