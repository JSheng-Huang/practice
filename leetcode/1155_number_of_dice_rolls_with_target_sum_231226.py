"""LeetCode#1155(Medium) Number of Dice Rolls With Target Sum
Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/?envType=daily-question&envId=2023-12-26
Problem:
        You have n dice, and each die has k faces numbered from 1 to k.
        Given three integers n, k, and target, return the number of possible 
    ways (out of the kn total ways) to roll the dice, so the sum of the face-up 
    numbers equals target. Since the answer may be too large, return it modulo 
    109 + 7.
Example:
    #1:
      Input: n = 1, k = 6, target = 3
      Output: 1
      Explanation: 
            You throw one die with 6 faces.
            There is only one way to get a sum of 3.
    #2:
      Input: n = 2, k = 6, target = 7
      Output: 6
      Explanation: 
            You throw two dice, each with 6 faces.
            There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
    #3:
      Input: n = 30, k = 30, target = 500
      Output: 222616187
      Explanation: The answer must be returned modulo 10^9 + 7.
Constraints: 
    #1. 1 <= n, k <= 30
1 <= target <= 1000
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Date: 231226.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        pass


if __name__ == '__main__':
    qwe = Solution()

    """Should return `1`."""
    print(qwe.numRollsToTarget(1, 6, 3))

    """Should return `6`."""
    print(qwe.numRollsToTarget(2, 6, 7))

    """Should return `222616187`."""
    print(qwe.numRollsToTarget(30, 30, 500))
