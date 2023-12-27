"""LeetCode#1155(Medium) Number of Dice Rolls With Target Sum
Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/?envType=daily-question&envId=2023-12-26
Problem:
        You have n dice, and each die has k faces numbered from 1 to k.
        Given three integers n, k, and target, return the number of possible 
    ways (out of the kn total ways) to roll the dice, so the sum of the face-up 
    numbers equals target. Since the answer may be too large, return it modulo 
    10^9 + 7.
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
    #2. 1 <= target <= 1000
Refer to: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/solutions/822515/python-3-dp-explanation/?envType=daily-question&envId=2023-12-26
    Time Complexity: O(n * k * target)?
    Space Complexity: O((target + 1) ** 2)?
Date: 231226.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Handle special case, it speed things up, but not necessary."""
        if n * k < target:
            return 0
        """Handle special case, it speed things up, but not necessary."""
        if n * k == target:
            return 1
        mod = int(10 ** 9 + 7)

        """
        `dp[i][j]` means the current sum is `j` after throwing the i-th dice.
        """
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for j in range(1, min(k + 1, target + 1)):
            dp[1][j] = 1
        """
        `i`: The current number of using dice(`n`), from 2 to `n`, `n + 1` 
             because of using for-loop indexing.
        `j`: The current number of `target`, from 1 to `target`., `target + 1` 
             because of using for-loop indexing.
        `k`: The current number of upper limit of a die(`k`), from 1 to `k`, 
             `k + 1` because of using for-loop indexing.
        """
        for i in range(2, n + 1):
            for j in range(1, target + 1):
                """
                In `k` for-looping, it finds all positive integers which is 
                less or equal to `j`, each one of them is one of the 
                possibilities to combine `j`.
                """
                for k in range(1, k + 1):
                    if j - k >= 0:
                        """
                        Sum the total possibilities from `j - 1`(coz `k` is `1` 
                        at least) to `0`.
                        """
                        dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= mod
        """
        Values in `dp` by using `n = 2`, `k = 6` and `target = 7` as the input:
        [[0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 1, 1, 1, 1, 1, 1, 0], 
         [0, 0, 1, 2, 3, 4, 5, 6]]
        """
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    qwe = Solution()

    """Should return `1`."""
    # print(qwe.numRollsToTarget(1, 6, 3))

    """Should return `6`."""
    print(qwe.numRollsToTarget(2, 6, 7))

    """Should return `222616187`."""
    # print(qwe.numRollsToTarget(30, 30, 500))
