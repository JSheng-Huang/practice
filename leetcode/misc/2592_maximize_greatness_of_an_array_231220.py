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
Refer to: https://leetcode.com/problems/maximize-greatness-of-an-array/solutions/3312061/java-c-python-easy-and-concise-o-n/
    Time Complexity: O(n).
    Space Complexity: O(n).
Date: 231220.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional

# # for importing built-in functions.
from collections import Counter


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        """My understanding from the reference.
        Except for highest frequency `num`, other `num` could find a smaller one to satisfy the requirement, or use the highest frequency `num` to do so.
        e.g.:
            Input: `nums = [1, 3, 3, 4, 5]`
            Assign: `res = 0`
            1. Remove `3` because it's frequency is the highest:
                `rest_nums = [3, 3]`
                `to_be_paired_nums = [1, 4, 5]`
            2. Except for `1`, others could find a suitable number to satisfy the requirement:
                2.1 `5` could use `4` or `1` to pair, so `res += 1`.
                2.2 `4` could use `1` to pair, so `res += 1`.
                2.3 Currently, two lists become:
                    `rest_nums = [3, 3]`
                    `to_be_paired_nums = [1]`
            3. Use `1` as the smaller one to pair one `3` in `rest_nums`, so two lists become:
                `rest_nums = [3]`
                `to_be_paired_nums = [1]`
            4. Conclude step 1 to 3:
                # `max_num_freq` is `2`(the number of `3` appears in `nums`).
                # `len(rest_nums)` and `len(to_be_paired_nums)` are 
                # complementary, so use `max_num_freq` to be the subtrahend.
                `res = len(nums) - max_num_freq`
        """
        return len(nums) - max(Counter(nums).values())

    def maximizeGreatness(self, nums: List[int]) -> int:
        """
        Modify from the reference for avoid importing extra built-in functions.
        """
        nums_dict = {}
        max_num_freq = 0
        for num in nums:
            
        return len(nums) - max(Counter(nums).values())


if __name__ == '__main__':
    qwe = Solution()

    """Should return `4`."""
    print(qwe.maximizeGreatness([1, 3, 5, 2, 1, 3, 1]))

    """Should return `3`."""
    print(qwe.maximizeGreatness([1, 2, 3, 4]))
