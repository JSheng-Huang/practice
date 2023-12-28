"""LeetCode#1531(Hard) String Compression II
Link: https://leetcode.com/problems/string-compression-ii/?envType=daily-question&envId=2023-12-28
Problem:
        `Run-length encoding`(https://en.wikipedia.org/wiki/Run-length_encoding) is a string compression method that works by 
    replacing consecutive identical characters (repeated 2 or more times) with 
    the concatenation of the character and the number marking the count of the 
    characters (length of the run). For example, to compress the string 
    "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the 
    compressed string becomes "a2bc3".
        Notice that in this problem, we are not adding '1' after single 
    characters.
        Given a string s and an integer k. You need to delete at most k 
    characters from s such that the run-length encoded version of s has minimum 
    length.
        Find the minimum length of the run-length encoded version of s after 
    deleting at most k characters.
Example:
    #1:
      Input: s = "aaabcccd", k = 2
      Output: 4
      Explanation: 
            Compressing s without deleting anything will give us "a3bc3d" of 
        length 6. Deleting any of the characters 'a' or 'c' would at most 
        decrease the length of the compressed string to 5, for instance delete 
        2 'a' then we will have s = "abcccd" which compressed is abc3d. 
        Therefore, the optimal way is to delete 'b' and 'd', then the 
        compressed version of s will be "a3c3" of length 4.
    #2:
      Input: s = "aabbaa", k = 2
      Output: 2
      Explanation: 
            If we delete both 'b' characters, the resulting compressed string 
        would be "a4" of length 2.
    #3:
      Input: s = "aaaaaaaaaaa", k = 0
      Output: 3
      Explanation: 
            Since k is zero, we cannot delete anything. The compressed string 
        is "a11" of length 3.
Constraints: 
    #1. 1 <= s.length <= 100
    #2. 0 <= k <= s.length
    #3. s contains only lowercase English letters.
Refer to: https://leetcode.com/problems/string-compression-ii/solutions/2704634/python-with-comments/?envType=daily-question&envId=2023-12-28
    Time and Space Complexity(The author said so?): 
        O(n ^ 2 * 26 * k) = O(n ^ 2 * k).
Date: 231228.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """Used to store all possibilities."""
        memo = {}

        """
        1st param: The compressed string `s`.
        2nd param: Start from which index of `s`.
        3rd param: You could remove `k` characters at most from `s`.
        4th param: The previous character.
        5th param: The run-length of the previous character.
        """
        return self.dfs(s, 0, k, None, 0, memo)

    def dfs(self, s, i, k, prev, l, memo):
        if i == len(s):
            return 0
        """The result has been found once."""
        if (i, k, prev, l) in memo:
            return memo[(i, k, prev, l)]
        """Check the quota(`k`) has been run out or not."""
        if k > 0:
            delete = self.dfs(s, i + 1, k - 1, prev, l, memo)
        else:
            delete = float("inf")
        if s[i] == prev:
            """
            Need one more digit to carry for the count.
            If `l == 1`: E.g. `j` => `j2`.
            If `len(str(l + 1)) > len(str(l))`: E.g. `j9` => `j10`.
            """
            if (l == 1) or (len(str(l + 1)) > len(str(l))):
                carry = 1
            else:
                carry = 0
            skip = carry + self.dfs(s, i + 1, k, s[i], l + 1, memo)
        else:
            skip = 1 + self.dfs(s, i + 1, k, s[i], 1, memo)
        """To delete, or not to delete."""
        memo[(i, k, prev, l)] = min(delete, skip)

        """To think this part."""
        return memo[(i, k, prev, l)]


if __name__ == '__main__':
    qwe = Solution()

    """Should return `4`."""
    print(qwe.getLengthOfOptimalCompression('aaabcccd', 2))

    """Should return `2`."""
    # print(qwe.getLengthOfOptimalCompression('aabbaa', 2))

    """Should return `3`."""
    # print(qwe.getLengthOfOptimalCompression('aaaaaaaaaaa', 0))
