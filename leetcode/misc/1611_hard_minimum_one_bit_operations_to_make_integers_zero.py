"""LeetCode#1611(Hard) Minimum One Bit Operations to Make Integers Zero
Link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30
Problem:
        Given an integer n, you must transform it into 0 using the following 
    operations any number of times:
        Change the rightmost (0th) bit in the binary representation of n.
        Change the ith bit in the binary representation of n if the (i-1)th bit 
    is set to 1 and the (i-2)th through 0th bits are set to 0.
        Return the minimum number of operations to transform n into 0.
Constraints: 0 <= n <= 109.
Example:
    #1:
      Input: n = 3
      Output: 2
      Explanation: The binary representation of 3 is "11".
        "11" -> "01" with the 2nd operation since the 0th bit is 1.
        "01" -> "00" with the 1st operation.
    #2:
      Input: n = 6
      Output: 4
      Explanation: The binary representation of 6 is "110".
        "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th 
        through 0th bits are 0.
        "010" -> "011" with the 1st operation.
        "011" -> "001" with the 2nd operation since the 0th bit is 1.
        "001" -> "000" with the 1st operation.
Refer to:
    #1. 
    Time Complexity: O(log(n)).
    Space Complexity: O(1).
    #2. https://zxi.mytechroad.com/blog/math/leetcode-1611-minimum-one-bit-operations-to-make-integers-zero/
    Time Complexity: O(log(n)).
    Space Complexity: O(1).
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """#1"""
        bin_n = format(n, 'b')
        bit_num = len(bin_n)
        res = 0
        for i in range(1, bit_num + 1):
            if bin_n[-i] == '1':
                res = 2 ** i - 1 - res

        """#2. Graycode: Ans is the order of `n` in Graycode."""
        # while n:
        #     res ^= n
        #     n >>= 1

        return res


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.minimumOneBitOperations(84))
