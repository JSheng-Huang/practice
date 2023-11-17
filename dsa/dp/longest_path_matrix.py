"""Longest Path in Matrix
Problem:
        Given a `n * n` matrix where all numbers are distinct, find the maximum 
    length path (starting from any cell) such that all cells along the path are 
    in increasing order with a difference of 1. We can move in 4 directions 
    from a given cell (i, j), i.e., we can move to (i + 1, j) or (i, j + 1) or 
    (i - 1, j) or (i, j - 1) with the condition that the adjacent cells have a 
    difference of 1.
Example:
    Input: mat[][] = {{1, 2, 9},
                      {5, 3, 8},
                      {4, 6, 7}}
    Output: 4
    The longest path is 6-7-8-9.
Refer to:
    1. https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
    Time Complexity: O(n^2), all values of dp[i][j] are computed only once.
    Space Complexity: O(n^2), since n * n extra space has been taken.
Created by JSheng <jasonhuang0124@gmail.com>"""


def findLongestPathFromEachCell(i, j, sqr_mat, sqr_mat_size, dp):
    """Out of Bound."""
    if i < 0 or i >= sqr_mat_size or j < 0 or j >= sqr_mat_size:
        return 0
    """The sub-problem is already solved."""
    if dp[i][j] != -1:
        return dp[i][j]
    """
    To store the path lengths in all the four directions, set them as `1` because if none of the adjacent fours is one greater we will take `1`.
    """
    e, w, s, n = 1, 1, 1, 1

    """
    Since all numbers are unique and in range from 1 to n * n, there is at most 
    one possible direction from any cell.
    """
    if (j < sqr_mat_size - 1 and ((sqr_mat[i][j] + 1) == sqr_mat[i][j + 1])):
        e = 1 + \
            findLongestPathFromEachCell(i, j + 1, sqr_mat, sqr_mat_size, dp)
    if (j > 0 and (sqr_mat[i][j] + 1 == sqr_mat[i][j - 1])):
        w = 1 + \
            findLongestPathFromEachCell(i, j - 1, sqr_mat, sqr_mat_size, dp)
    if (i < sqr_mat_size - 1 and (sqr_mat[i][j] + 1 == sqr_mat[i + 1][j])):
        s = 1 + \
            findLongestPathFromEachCell(i + 1, j, sqr_mat, sqr_mat_size, dp)
    if (i > 0 and (sqr_mat[i][j] + 1 == sqr_mat[i - 1][j])):
        n = 1 + \
            findLongestPathFromEachCell(i - 1, j, sqr_mat, sqr_mat_size, dp)
    """
    If none of the adjacent fours is one greater we will take `1`, otherwise we 
    will pick maximum from all the four directions.
    """
    dp[i][j] = max(e, w, s, n)
    return dp[i][j]


def findLongestPathOverAll(sqr_mat, sqr_mat_size):
    """Default."""
    result = 1

    dp = [[-1 for _ in range(sqr_mat_size)]for _ in range(sqr_mat_size)]
    for i in range(sqr_mat_size):
        for j in range(sqr_mat_size):
            if (dp[i][j] == -1):
                findLongestPathFromEachCell(i, j, sqr_mat, sqr_mat_size, dp)
            result = max(result, dp[i][j])
    return result


if __name__ == '__main__':
    sqr_mat = [[5, 2, 9],
               [1, 3, 8],
               [4, 6, 7]]
    sqr_mat_size = 3
    print("Length of the longest path is ",
          findLongestPathOverAll(sqr_mat, sqr_mat_size))
