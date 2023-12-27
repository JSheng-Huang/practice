"""LeetCode#1578(Medium) Minimum Time to Make Rope Colorful
Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/?envType=daily-question&envId=2023-12-27
Problem:
        Alice has n balloons arranged on a rope. You are given a 0-indexed 
    string colors where colors[i] is the color of the ith balloon.
        Alice wants the rope to be colorful. She does not want two consecutive 
    balloons to be of the same color, so she asks Bob for help. Bob can remove 
    some balloons from the rope to make it colorful. You are given a 0-indexed 
    integer array neededTime where neededTime[i] is the time (in seconds) that 
    Bob needs to remove the ith balloon from the rope.
        Return the minimum time Bob needs to make the rope colorful.
Example:
    #1:
      Input: colors = "abaac", neededTime = [1,2,3,4,5]
      Output: 3
      Explanation: 
            In the above image, 'a' is blue, 'b' is red, and 'c' is green.
            Bob can remove the blue balloon at index 2. This takes 3 seconds.
            There are no longer two consecutive balloons of the same color. 
        Total time = 3.
    #2:
      Input: colors = "abc", neededTime = [1,2,3]
      Output: 0
      Explanation: 
            The rope is already colorful. Bob does not need to remove any 
        balloons from the rope.
    #3:
      Input: colors = "aabaa", neededTime = [1,2,3,4,1]
      Output: 2
      Explanation: 
            Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 
        second to remove.
            There are no longer two consecutive balloons of the same color. 
        Total time = 1 + 1 = 2.
Constraints: 
    #1. n == colors.length == neededTime.length
    #2. 1 <= n <= 105
    #3. 1 <= neededTime[i] <= 104
    #4. colors contains only lowercase English letters.
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Date: 231227.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        if the current one is as same as the next one, find til next one is not
        3 by 3
        """
        res = 0
        c_len = len(colors)
        for i in range(c_len - 1):
            cur_c = colors[i]
            nxt_idx = i + 1
            while (nxt_idx < c_len) and (cur_c == colors[nxt_idx]):
                nxt_idx += 1
        pass


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[1,2,3,4,5]`."""
    print(qwe.minCost('abaac'))

    """Should return `[1,2,3]`."""
    print(qwe.minCost('abc'))

    """Should return `[1,2,3,4,1]`."""
    print(qwe.minCost('aabaa'))
