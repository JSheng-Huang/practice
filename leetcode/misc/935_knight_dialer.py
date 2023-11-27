"""LeetCode#4(Hard) Median of Two Sorted Arrays
Link: https://leetcode.com/problems/knight-dialer/?envType=daily-question&envId=2023-11-27
Problem:
    The chess knight has a unique movement, it may move two squares vertically 
and one square horizontally, or two squares horizontally and one square 
vertically (with both forming the shape of an L).
    Given an integer n, return how many distinct phone numbers of length n we 
can dial.
    You are allowed to place the knight on any numeric cell initially and then 
you should perform n - 1 jumps to dial a number of length n. All jumps should 
be valid knight jumps.
    As the answer may be very large, return the answer modulo 10 ^ 9 + 7.
Constraints: 1 <= n <= 5000
Example:
    #1:
      Input: n = 1
      Output: 10
      Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
    #2:
      Input: n = 2
      Output: 20
      Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
    #3:
      Input: n = 3131
      Output: 136006598
      Explanation: Please take care of the mod.
Refer to:
    #1. 
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def knightDialer(self, n: int) -> int:
        pass


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.knightDialer([1, 3], [2]))
