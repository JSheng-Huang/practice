"""Longest Common Subsequence
Definition:
    A longest common subsequence is defined as the longest subsequence
which is common in all given input sequences.
Problem:
    There are two sorted arrays nums1 and nums2 of size `m` and `n` 
respectively. Find the median of the two sorted arrays. The overall run 
time complexity should be O(log(m + n)).
Refer to:
    1. https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
    Time Complexity: O(m * n), where `m` and `n` are sizes of two arrays.
    Space Complexity: O(m), because the algorithm uses two arrays of size `m`.
Created by JSheng <jasonhuang0124@gmail.com>"""


def longestCommonSubsequence(text1, text2):
    t1 = len(text1)
    t2 = len(text2)

    """`text1` must be the longer one for the following operation."""
    if t1 < t2:
        longestCommonSubsequence(text2, text1)
    prev = [0] * (t1 + 1)
    cur = [0] * (t1 + 1)
    for idx2 in range(1, t2 + 1):
        for idx1 in range(1, t1 + 1):
            # If characters are matching
            if text2[idx2 - 1] == text1[idx1 - 1]:
                cur[idx1] = 1 + prev[idx1 - 1]
            else:
                # If characters are not matching
                cur[idx1] = max(cur[idx1 - 1], prev[idx1])

        prev = cur.copy()

    return cur[t1]


if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print("Length of LCS is", longestCommonSubsequence(S1, S2))
    print("Length of LCS is", longestCommonSubsequence(S2, S1))
