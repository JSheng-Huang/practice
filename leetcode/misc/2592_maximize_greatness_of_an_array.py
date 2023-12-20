"""LeetCode#2900(Medium) 2592. Maximize Greatness of an Array
Link: https://leetcode.com/problems/maximize-greatness-of-an-array/
Problem:
        You are given a 0-indexed integer array `nums`. You are allowed to 
    permute `nums` into a new array perm of your choosing.
        We define the greatness of nums be the number of indices 0 <= i < nums.
    length for which perm[i] > nums[i].
        Return the maximum possible greatness you can achieve after permuting 
    nums.
Example:
    #1:
      Input: nums = [1,3,5,2,1,3,1]
      Output: 4
      Explanation: 
            One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
            At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
    #2:
      Input: nums = [1,2,3,4]
      Output: 3
      Explanation: 
            We can prove the optimal perm is [2,3,4,1].
            At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.
Constraints: 
    #1. 1 <= nums.length <= 105
    #2. 0 <= nums[i] <= 109
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
    Explanation: ???
Date: 231220.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        res = 0
        nums_max = max(nums)
        nums_min = min(nums)
        for num in nums:
            if num != nums_max or num != nums_min:
                res += 1
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Should return `4`."""
    print(qwe.maximizeGreatness([1, 3, 5, 2, 1, 3, 1]))

    """Should return `3`."""
    print(qwe.maximizeGreatness([1, 2, 3, 4]))
