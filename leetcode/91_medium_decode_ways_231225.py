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
Refer to: https://leetcode.com/problems/decode-ways/solutions/4454026/beats-99-optimal-linear-solution-video-walkthrough/?envType=daily-question&envId=2023-12-25
    Time Complexity: O(n).
    Space Complexity: O(1).
Date: 231225.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0':
            return 0
        dp_2 = 1

        dp_1 = int(s[-1] != '0')
        print(s[-1] != '0')
        print(dp_1)
        print()
        """from the second to last"""
        i = len(s) - 2
        while i >= 0:
            """
            dp_0: from i to n
            dp_1: s[i] is single
            dp_2: s[i] is 1st of bi
            """
            if s[i] == '0':
                dp_0 = 0
            else:
                dp_0 = dp_1
                """If """
                if (s[i] == '1') or (s[i] == '2' and int(s[i + 1]) < 7):
                    dp_0 += dp_2
            dp_2 = dp_1
            dp_1 = dp_0
            dp_0 = 0
            i -= 1
        return dp_1


if __name__ == '__main__':
    qwe = Solution()

    """Should return `2`."""
    print(qwe.numDecodings("12"))

    """Should return `3`."""
    print(qwe.numDecodings("226"))

    """Should return `0`."""
    print(qwe.numDecodings("06"))

    """Should return `1`."""
    print(qwe.numDecodings("1"))

    """Should return `1`."""
    print(qwe.numDecodings("10"))

    """Should return `1`."""
    print(qwe.numDecodings("27"))

    """Should return `1`."""
    print(qwe.numDecodings("2101"))

    """Should return `3`."""
    print(qwe.numDecodings("1201234"))
