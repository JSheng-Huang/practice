"""LeetCode#191(Easy) Number of 1 Bits
Link: https://leetcode.com/problems/number-of-1-bits/
Problem:
        Write a function that takes the binary representation of an unsigned 
    integer and returns the number of '1' bits it has (also known as the 
    Hamming weight).
Note:
    #1. Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    #2. In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.    
Example:
    #1:
      Input: n = 00000000000000000000000000001011
      Output: 3
      Explanation: 
            The input binary string 00000000000000000000000000001011 has a 
        total of three '1' bits.
    #2:
      Input: n = 00000000000000000000000010000000
      Output: 1
      Explanation: 
            The input binary string 00000000000000000000000010000000 has a 
        total of one '1' bit.
    #3:
      Input: n = 11111111111111111111111111111101
      Output: 31
      Explanation: 
            The input binary string 11111111111111111111111111111101 has a 
        total of thirty one '1' bits.
Constraints: The input must be a binary string of length 32.
Refer to: https://github.com/azl397985856/leetcode/blob/master/problems/191.number-of-1-bits.md
Time Complexity: O(log(n))
Space Complexity: O(n)
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.hammingWeight(int('00000000000000000000000010000000', 2)))
