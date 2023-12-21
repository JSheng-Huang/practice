"""LeetCode#763(Medium) Partition Labels
Link: https://leetcode.com/problems/partition-labels/
Problem:
        You are given a string s. We want to partition the string into as many 
    parts as possible so that each letter appears in at most one part.
        Note that the partition is done so that after concatenating all the 
    parts in order, the resultant string should be s.
        Return a list of integers representing the size of these parts.
Example:
    #1:
      Input: s = "ababcbacadefegdehijhklij"
      Output: [9,7,8]
      Explanation:
            The partition is "ababcbaca", "defegde", "hijhklij".
            This is a partition so that each letter appears in at most one part.
            A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
        because it splits s into less parts.
    #2:
      Input: s = "eccbbbbdec"
      Output: [10]
Constraints: 
    #1. 1 <= s.length <= 500
    #2. `s` consists of lowercase English letters.
Refer to: https://leetcode.com/problems/partition-labels/solutions/1868757/python3-greedy-validation-explained/
    Note: 
        I use the solution in the comments which are below the reference, they 
    are same concept.
    Time Complexity: O(n).
    Space Complexity: O(1).
    Explanation: For the space complexity, the hashmap consist of max 26 keys.
Date: 231221.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Since each letter can appear only in one part, we cannot form a part 
        shorter than the index of the last appearance of a letter subtracted by 
        an index of the first appearance. For example here (`absfab`) the 
        lengths of the first part are limited by the positions of the letter a. 
        So it's important to know at what index each letter appears in the 
        string last time. We can create a hash map and fill it with the last 
        indexes for letters.
        Also, we have to validate a candidate part. For the same example 
        (`absfab`) we see that letter a cannot form a border for the first part 
        because of a nasty letter b inside. So we need to expand the range of 
        the initial part.
        """
        res = []
        end_idx = 0
        last_idx_dict = {}
        s_len = len(s)

        """Keep the last indices of characters in `s`."""
        for i in range(s_len):
            last_idx_dict[s[i]] = i
        for i in range(s_len):
            """
            Update `end_idx` if the last time of `s[i]` appears behind 
            `end_idx`.
            """
            if end_idx < last_idx_dict[s[i]]:
                end_idx = last_idx_dict[s[i]]
            """`s[i]` has reached its last time which it appears in `s`."""
            if end_idx == i:
                """`+1`: Because we use indices to compute."""
                res.append(end_idx - sum(res) + 1)
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[9,7,8]`."""
    print(qwe.partitionLabels('ababcbacadefegdehijhklij'))

    """Should return `[10]`."""
    print(qwe.partitionLabels('eccbbbbdec'))

    """Should return `[1,12,1,1]`."""
    print(qwe.partitionLabels('jpsegvwolkpystd'))
