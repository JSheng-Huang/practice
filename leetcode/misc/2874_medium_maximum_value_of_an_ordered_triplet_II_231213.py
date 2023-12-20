"""LeetCode#2874(Medium) Maximum Value of an Ordered Triplet II
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
Problem:
        You are given a 0-indexed integer array nums.
        Return the maximum value over all triplets of indices (i, j, k) such 
    that i < j < k. If all such triplets have a negative value, return 0.
        The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums
    [j]) * nums[k].
Example:
    #1:
      Input: nums = [12,6,1,2,7]
      Output: 77
      Explanation: 
            The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] 
        = 77.
            It can be shown that there are no ordered triplets of indices with 
        a value greater than 77. 
    #2:
      Input: nums = [1,10,3,4,19]
      Output: 133
      Explanation: 
            The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] 
        = 133.
            It can be shown that there are no ordered triplets of indices with 
        a value greater than 133.
    #3:
      Input: nums = [1,2,3]
      Output: 0
      Explanation: 
            The only ordered triplet of indices (0, 1, 2) has a negative value 
        of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
Constraints: 
    #1. 3 <= nums.length <= 105
    #2. 1 <= nums[i] <= 106
Refer to: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/solutions/4111962/java-c-python-one-pass-o-n/
    Time Complexity: O(n).
    Space Complexity: O(1).
Date: 231213.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_num = 0
        max_diff = 0
        for num in nums:
            """
            The order matters, `res` must be put in the front of `max_diff` for 
            the case which the length of `nums` is `3` and the maximum is not 
            at `nums[2]`, because `max_diff` would be updated wrongly in the 
            3-th loop by using `nums[2]` as `j`, which is mentioned in the 
            question. 
            The order of `max_nums` does not matter, if it is updated:
                #1. `max_diff` would not be updated, because the current `num` 
                is the maximum.
                #2. `res` always takes the current `num` as the maximum, so they are irrelevant.
            """
            res = max(res, max_diff * num)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Should return `77`."""
    print(qwe.maximumTripletValue([12, 6, 1, 2, 7]))

    """Should return `133`."""
    print(qwe.maximumTripletValue([1, 10, 3, 4, 19]))

    """Should return `0`."""
    print(qwe.maximumTripletValue([1, 2, 3]))

    """Should return `0`."""
    print(qwe.maximumTripletValue([2, 3, 1]))

    """Should return `1`."""
    print(qwe.maximumTripletValue([3, 2, 1]))
