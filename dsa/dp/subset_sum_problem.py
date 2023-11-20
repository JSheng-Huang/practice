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


# Returns True if there is a subset of set[]
# with a sum equal to the given sum
def isSubsetSum(nums, n, sum):
    # Create a list to store the previous row result
    prev = [False] * (sum + 1)

    # If sum is 0, then the answer is True
    prev[0] = True

    # If sum is not 0 and the set is empty,
    # then the answer is False
    """Why???"""
    for i in range(1, n + 1):
        curr = [False] * (sum + 1)
        for j in range(1, sum + 1):
            if j < nums[i - 1]:
                curr[j] = prev[j]
            if j >= nums[i - 1]:
                print('i', i)
                print('j', j)
                print('prev[j]', prev[j])
                print('prev[j - nums[i - 1]', prev[j - nums[i - 1]])
                curr[j] = prev[j] or prev[j - nums[i - 1]]
                print(curr)
                print('---')
        # Now curr becomes prev for (i+1)-th element
        prev = curr
        print('===')
    return prev[sum]


# Driver code
if __name__ == '__main__':
    nums = [3, 34, 4, 12, 5, 2]
    sum_value = 9
    n = len(nums)
    if isSubsetSum(nums, n, sum_value):
        print("Found a subset with the given sum")
    else:
        print("No subset with the given sum")
