"""LeetCode#1375(Medium) Number of Times Binary String Is Prefix-Aligned
Link: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/
Problem:
        You have a 1-indexed binary string of length n where all the bits are 0 
    initially. We will flip all the bits of this binary string (i.e., change 
    them from 0 to 1) one by one. You are given a 1-indexed integer array flips 
    where flips[i] indicates that the bit at index i will be flipped in the ith 
    step.
        A binary string is prefix-aligned if, after the ith step, all the bits 
    in the inclusive range [1, i] are ones and all the other bits are zeros.
        Return the number of times the binary string is prefix-aligned during 
    the flipping process.
Note: N/A.
Example:
    #1:
      Input: flips = [3,2,4,1,5]
      Output: 2
      Explanation: 
            The binary string is initially "00000".
            After applying step 1: The string becomes "00100", which is not 
        prefix-aligned.
            After applying step 2: The string becomes "01100", which is not 
        prefix-aligned.
            After applying step 3: The string becomes "01110", which is not 
        prefix-aligned.
            After applying step 4: The string becomes "11110", which is 
        prefix-aligned.
            After applying step 5: The string becomes "11111", which is 
        prefix-aligned.
            We can see that the string was prefix-aligned 2 times, so we return 
        2.
    #2:
      Input: flips = [4,1,2,3]
      Output: 1
      Explanation: 
            The binary string is initially "0000".
            After applying step 1: The string becomes "0001", which is not 
        prefix-aligned.
            After applying step 2: The string becomes "1001", which is not 
        prefix-aligned.
            After applying step 3: The string becomes "1101", which is not 
        prefix-aligned.
            After applying step 4: The string becomes "1111", which is 
        prefix-aligned.
            We can see that the string was prefix-aligned 1 time, so we return 
        1.
Constraints: 
    #1. n == flips.length
    #2. 1 <= n <= 5 * 104
    #3. `flips` is a permutation of the integers in the range [1, n].
Refer to: 
    #1. https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/solutions/532538/java-c-python-straight-forward-o-1-space/
    Time Complexity: O(n).
    Space Complexity: O(1).
    #2. https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/solutions/2884695/python-3-6-lines-w-explanation-t-m-90-96/
    Time Complexity: O(n).
    Space Complexity: O(1).
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        """TLE(Myself): Do not need to use exponentiation."""
        n = len(flips)
        bin_sum = 0
        cur_sum = 0
        res = 0
        for i in range(n - 1, -1, -1):
            bin_sum += 2 ** i
            cur_sum += 2 ** (n - flips[n - i - 1])
            if bin_sum == cur_sum:
                res += 1
        return res

    def numTimesAllBlue(self, flips: List[int]) -> int:
        """
        `right` is the number of the right most lighted bulb.
        Iterate the input light `flips`, update `right = max(right, flips[i])`.
        Now we have lighted up `i + 1` bulbs, if `right == i + 1`, it means
        that all the previous bulbs (to the left) are turned on too. Then we
        increment `res`.
        """
        right = res = 0
        for i, val in enumerate(flips, 1):
            right = max(right, val)
            res += (right == i)
        return res

    def numTimesAllBlue(self, flips: List[int]) -> int:
        """
        The binary string is prefix-aligned if and only if the flips comprise a 
        set of consecutive integers beginning with one(123 is valid, 234 or 125 
        is not).
        The indices will always comprise a set of consecutive integers 
        beginning with zero.
        The binary string is prefix-aligned after k flips if and only if sum(i
        +1) = sum(flips[:i+1]) for i < k.
        """
        ans = 0
        f_sum = 0
        i_sum = 0
        for i, flip in enumerate(flips, start=1):
            f_sum += flip
            i_sum += i + 1
            ans += (i_sum == f_sum)
        return ans


if __name__ == '__main__':
    qwe = Solution()

    """Return `2`."""
    print(qwe.numTimesAllBlue([3, 2, 4, 1, 5]))

    """Return `1`."""
    print(qwe.numTimesAllBlue([4, 1, 2, 3]))
