"""LeetCode#1611(Hard) Minimum One Bit Operations to Make Integers Zero
Link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30
Problem:
        Given an integer n, you must transform it into 0 using the following 
    operations any number of times:
        Change the rightmost (0th) bit in the binary representation of n.
        Change the ith bit in the binary representation of n if the (i-1)th bit 
    is set to 1 and the (i-2)th through 0th bits are set to 0.
        Return the minimum number of operations to transform n into 0.
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
Constraints: 0 <= n <= 109.
Refer to:
    #1. https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/solutions/4344637/c-python-java-explained/?envType=daily-question&envId=2023-11-30
    Time Complexity: O(log(n)).
    Space Complexity: O(1).
    #2. https://zxi.mytechroad.com/blog/math/leetcode-1611-minimum-one-bit-operations-to-make-integers-zero/
    Time Complexity: O(log(n)).
    Space Complexity: O(1).
Date: 231130.
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """#1.
        Assume a number 1101001
        Starting from left to right to save number of operations
            1000000->0 takes 2 ** 7 - 1 = 127 steps
            0100000->0 takes 2 ** 6 - 1 = 63 steps
            0001000->0 takes 2 ** 4 - 1 = 15 steps
            0000001->0 takes 2 ** 1 - 1 = 1 step
        Hence can be said
            1(2 ** 0 - 1) -> 0 needs 1 operation,
            2(2 ** 1 - 1) -> 0 needs 3 operations,
            4(2 ** 2 - 1) -> 0 needs 7 operations,
        2 ** k needs 2 ** (k + 1) - 1 operations.
        Approach
            1101001: Required steps = 127 - 63 + 15 - 1 = 78
        Let steps x to convert 000000 to 100000.
        But, since 1101001 already has 1 in the 5th bit from right, some steps 
        will be saved.
        Saved steps y = Number of steps needed to convert 000000 to 100000
        Hence not all the 2^(6+1) - 1 steps to convert 1000000 -> 0 as 0100000 can be obtained in less number of steps.
            For 0100000 -> 0, we need to add its 2 ** 6 - 1 steps
            For 0001000 -> 0, we need to add its 2 ** 4 - 1 steps
            For 0000001 -> 0, we need to add its 2 ** 1 - 1 steps
        Result = (2 ** 7 - 1) - (2 ** 6 - 1) + (2 ** 4 - 1) - (2 ** 1 - 1)
        Note that: 
            n &= n-1; make us go to the next bit 1 from right to left 
        (least significant).
            n = 010100;
            n &= n-1;  010100 & 010011
            n = 010000;
        Reason for abs():
            You just need to assure that the steps are added by one time + and 
        one time - repetitively from left to right or right to left, the 
        absolute value of answer is correct.
        """
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)
        """#2. Graycode: Ans is the order of `n` in Graycode."""
        # while n:
        #     res ^= n
        #     n >>= 1

        # return res


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.minimumOneBitOperations(105))
