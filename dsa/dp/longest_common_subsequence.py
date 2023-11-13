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
    t1_len = len(text1)
    t2_len = len(text2)

    """`text1` must be the longer one for the following operation."""
    if t1_len < t2_len:
        longestCommonSubsequence(text2, text1)
    prev = [0] * (t1_len + 1)
    cur = [0] * (t1_len + 1)
    for i in range(1, t2_len + 1):
        for j in range(1, t1_len + 1):
            if text2[i - 1] == text1[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                cur[j] = max(cur[j - 1], prev[j])
        prev = cur.copy()
    return cur[-1]


if __name__ == '__main__':
    S1 = 'AGGTAB'
    S2 = 'GXTXAYB'
    print('Length of LCS is', longestCommonSubsequence(S1, S2))
