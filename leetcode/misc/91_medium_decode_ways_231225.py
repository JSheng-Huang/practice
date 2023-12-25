"""LeetCode#91(Medium) Decode Ways
Link: https://leetcode.com/problems/decode-ways/?envType=daily-question&envId=2023-12-25
Problem:
        A message containing letters from A-Z can be encoded into numbers using 
    the following mapping:
            'A' -> "1"
            'B' -> "2"
            ...
            'Z' -> "26"
        To decode an encoded message, all the digits must be grouped then 
    mapped back into letters using the reverse of the mapping above (there may 
    be multiple ways). For example, "11106" can be mapped into:
            "AAJF" with the grouping (1 1 10 6)
            "KJF" with the grouping (11 10 6)
        Note that the grouping (1 11 06) is invalid because "06" cannot be 
    mapped into 'F' since "6" is different from "06".
        Given a string s containing only digits, return the number of ways to 
    decode it.
        The test cases are generated so that the answer fits in a 32-bit 
    integer.
Example:
    #1:
      Input: s = "12"
      Output: 2
      Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
    #2:
      Input: s = "226"
      Output: 3
      Explanation: 
            "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 
        6).
    #3:
      Input: s = "06"
      Output: 0
      Explanation: 
            "06" cannot be mapped to "F" because of the leading zero ("6" is 
        different from "06").
Constraints: 
    #1. 1 <= s.length <= 100
    #2. s contains only digits and may contain leading zero(s).
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Date: 231225.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        226
        2 and 26: BZ
        22 and 6: VF
        2 and 2 and 6: BBF
        if 1st chac 0 => 0
        if 0 consecutively => 0
        if the chac before 0 must be 1 or 2, or => 0
        2 and 2 pairing?
        """
        """For the edge case."""
        if s[i] == 0:
            return 0
        n = len(s)
        res = 1
        for i in range(n):
            if s[i] == 0 and s[i - 1] == 0 or s[i - 1] > 2:
                return 0
            else:
                if s[i] == 1:
                    pass
                elif s[i] == 2:
                    pass
                elif s[i] == 0:
                    pass
                else:
                    pass
        """Before 1200"""


if __name__ == '__main__':
    qwe = Solution()

    """Should return `2`."""
    print(qwe.numDecodings("12"))

    """Should return `3`."""
    print(qwe.numDecodings("226"))

    """Should return `0`."""
    print(qwe.numDecodings("06"))
