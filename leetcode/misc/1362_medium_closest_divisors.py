"""LeetCode#1362(Medium) Closest Divisors
Link: https://leetcode.com/problems/closest-divisors/
Problem:
        Given an integer num, find the closest two integers in absolute 
    difference whose product equals num + 1 or num + 2.
        Return the two integers in any order.
Note: N/A.
Constraints: 1 <= num <= 10^9
Example:
    #1:
      Input: num = 8
      Output: [3,3]
      Explanation: 
            For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, 
        the closest divisors are 2 & 5, hence 3 & 3 is chosen.
    #2:
      Input: num = 123
      Output: [5,25]
      Explanation: N/A.
    #3:
      Input: num = 999
      Output: [40,25]
      Explanation: N/A.
Refer to: ???
Time Complexity: ???
Space Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        pass


if __name__ == '__main__':
    qwe = Solution()

    """Return `[3, 3]`."""
    print(qwe.closestDivisors(8))

    """Return `[5, 25]`."""
    print(qwe.closestDivisors(123))

    """Return `[40, 25]`."""
    print(qwe.closestDivisors(999))
