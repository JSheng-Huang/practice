"""LeetCode#1362(Medium) Closest Divisors
Link: https://leetcode.com/problems/closest-divisors/
Problem:
        Given an integer num, find the closest two integers in absolute 
    difference whose product equals num + 1 or num + 2.
        Return the two integers in any order.
Note: N/A.
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
Constraints: 1 <= num <= 10^9
Refer to: The following two authors use the same concept.
  #1. https://leetcode.com/problems/closest-divisors/solutions/517962/greedy-beat-100-time-memory/
  #2. https://leetcode.com/problems/closest-divisors/solutions/517595/java-c-python-easy-and-concise/
    Time Complexity: O(sqrt(n)).
    Space Complexity: O(1).
    Explanation: N/A.
Date: 231204.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        """
        Iterate candidates from int(sqrt(num+2)) to 1.
        Check num + 1 before num + 2. Because when a candidate i(1 might the 
        only one) is valid for both num + 1 and num + 2, The diff value of the 
        former is smaller.
        """
        for i in range(int((num + 2) ** 0.5), 0, -1):
            """`int()` would round down the parameter."""
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]


if __name__ == '__main__':
    qwe = Solution()

    """Return `[3, 3]`."""
    print(qwe.closestDivisors(8))

    """Return `[5, 25]`."""
    print(qwe.closestDivisors(123))

    """Return `[40, 25]`."""
    print(qwe.closestDivisors(999))

    """Return `[3, 3]`."""
    print(qwe.closestDivisors(7))

    """Return `[2, 3]`."""
    print(qwe.closestDivisors(4))
