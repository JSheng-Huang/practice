"""LeetCode#1862(Hard) Sum of Floored Pairs
Link: https://leetcode.com/problems/sum-of-floored-pairs/
Problem:
        Given an integer array nums, return the sum of floor(nums[i] / nums[j]) 
    for all pairs of indices 0 <= i, j < nums.length in the array. Since the 
    answer may be too large, return it modulo `10 ** 9 + 7`.
        The floor() function returns the integer part of the division.
Note: N/A.
Example:
    #1:
      Input: nums = [2,5,9]
      Output: 10
      Explanation:
            floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
            floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 3
            floor(5 / 2) = 2
            floor(9 / 2) = 4
            floor(9 / 5) = 1
            We calculate the floor of the division for every pair of indices in 
        the array then sum them up.
    #2:
      Input: nums = [7,7,7,7,7,7,7]
      Output: 49
Constraints: 
    #1. 1 <= nums.length <= 105
    #2. 1 <= nums[i] <= 105
Refer to: https://leetcode.com/problems/sum-of-floored-pairs/solutions/1218305/python-python3-solution-bruteforce-optimized-solution-using-dictionary/
    Time Complexity: N/A.
    Space Complexity: N/A.
    Explanation: N/A.
Date: 231215.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """TLE(Mine): Brute Force."""
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 2
                elif nums[i] > nums[j]:
                    res += (nums[i] // nums[j])
                else:
                    res += (nums[j] // nums[i])
        return (res + len(nums)) % (10 ** 9 + 7)

    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """
        The solution is built by using frequency of the prefix elements
        (frequency prefix sum).
            1. Take the frequency of the elements given in the nums and store 
            ir in dictionary.
            2. After storing calculate the prefix frequency of the nums 
            according to the frequency present in the dictionary.
            3. After computing prefix frequency just calculate the sum of the 
            floor division.
        """
        max_num_plus_1 = max(nums) + 1
        dic = {}
        prefix = [0] * max_num_plus_1
        res = 0
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        # print('dic', dic)
        for i in range(1, max_num_plus_1):
            if i not in dic:
                prefix[i] = prefix[i - 1]
            else:
                prefix[i] = prefix[i - 1] + dic[i]
        # print('prefix', prefix)
        # print('dic', dic)
        for i in set(nums):
            # print('i', i)
            """
            Because the step while looping is equal to `i`, `prefix[-1] - prefix
            [j - 1]` could be take as dividing. 
            `j - 1` matters, because `i` is 1 at least when `i` is divided by 
            itself.
            """
            for j in range(i, max_num_plus_1, i):
                res += dic[i] * (prefix[-1] - prefix[j - 1])
                # print('res', res)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    qwe = Solution()

    """Return `10`."""
    print(qwe.sumOfFlooredPairs([2, 5, 9]))

    """Return `49`."""
    print(qwe.sumOfFlooredPairs([7, 7, 7, 7, 7, 7, 7]))
