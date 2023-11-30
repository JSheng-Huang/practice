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
    Time Complexity: O(n).
    Space Complexity: O(1).
    #2. https://zxi.mytechroad.com/blog/math/leetcode-1611-minimum-one-bit-operations-to-make-integers-zero/
    Time Complexity: O(log(n)).
    Space Complexity: O(1).
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        to flip the bits to turn the number to zero

        Interpretation of Rules:
        - recursive:
            to turn a leading one of i bits to zero, the only way is to turn the i-1 bits to a leading one pattern
            and to turn the i-1 bits leading zero to zero, the only way is to turn the i-2 bits to a leading one pattern
            and so on, which is a recursive process

            (10000.. -> 11000.. -> 01000..), (01000.. -> 01100.. -> 00100), ..., (..010 -> ..011 -> ..001 -> ..000)

        - reversable:

            Let's make some observations to check if there's any pattern:

            - 2: 10 -> 11 -> 01 -> 00
            - 4: 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000
            - 8: 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> (reversing 100 to 000) -> 0000
            ...

            based on the observation, turning every i bits leading one to zero, is turning the i-1 bits from 00.. to 10..
            and then back to 00.., which is a reverable process, and with the recursive process we can conclude that
            turning any length of 00..M-> 10.. is a reversable process

        - all unique states:
            since it is recursive and reversable, and we are flipping every bit between 1 and 0 programtically 10.. <-> 00..
            we can conclude that every intermediate state in a process is unique (2**i unique states, so we need 2**i - 1 steps)

                for i bits 10.. <-> 00.. - numer of operations f(i) = 2**i - 1

            this also aligns with the observation above that f(i) = 2*f(i-1) - 1 (-1 for no operation needed to achieve the initial 000)

        Process:
        to turn any binary to 0, we can turning the 1s to 0s one by one from lower bit to higher bit
        and because turning a higher bit 1 to 0, would passing the unique state including the lower bit 1s
        we can reverse those operations needed for the higher bit 100.. to the unique state including the lower bit 1s

        e.g. turning 1010100 to 0
        - 1010(100) -> 1010(000), we will need 2**3 - 1 operations
        - 10(10000) -> 10(00000), we will need (2**5 - 1) - (2**3 - 1) operations
        we will be passing the state 10(10100), which is ready available from the last state
        so we can save/reverse/deduct the operations needed for 1010(000) <-> 1010(100)
        - ...

            so for any binary, f(binary) would tell us how many operations we need for binary <-> 000..
            and for any more 1s, 100{binary} we can regard it as a process of 100.. <-> 100{binary} <-> 000{000..}
            which is 100.. <-> 000.. (2**i - 1) saving the operations 100{000..} <-> 100{binary} (f(binary))
            = (2**i - 1) - f(last_binary)

        """
        binary = format(n, 'b')
        print(binary)
        N, res = len(binary), 0
        for i in range(1, N + 1):
            if binary[-i] == '1':
                res = 2 ** i - 1 - res
            print()
            print(res, format(res, 'b'))

        """#2. Graycode: Ans is the order of `n` in Graycode."""
        # while n:
        #     res ^= n
        #     n >>= 1

        return res


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.minimumOneBitOperations(84))
