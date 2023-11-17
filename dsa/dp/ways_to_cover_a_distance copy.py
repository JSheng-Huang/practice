"""Longest Path in Matrix
Problem:
        Given a n*n matrix where all numbers are distinct, find the maximum 
    length path (starting from any cell) such that all cells along the path are 
    in increasing order with a difference of 1. We can move in 4 directions 
    from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or 
    (i-1, j) or (i, j-1) with the condition that the adjacent cells have a 
    difference of 1.
Example:
    Input: mat[][] = {{1, 2, 9},
                      {5, 3, 8},
                      {4, 6, 7}}
    Output: 4
    The longest path is 6-7-8-9.
Refer to:
    1. https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
    Time Complexity: O(n2). It may seem more at first look. If we take a closer 
    look, we can notice that all values of dp[i][j] are computed only once.
    Space Complexity: O(N x N), since N x N extra space has been taken.
Created by JSheng <jasonhuang0124@gmail.com>"""


def wayToCoverDist(dist):
    way = [0] * 3

    """
    Initialize base values. There is one way({1}) to cover 0 and 1 distances 
    and two ways({1, 1} or {2}) to cover 2 distance.
    """
    way[0] = 1
    way[1] = 1
    way[2] = 2

    """Bottom-up Approach
    Sum up ways from `dist = 0` to `dist = n`, where `n` is the input.
    e.g., 'dist = 4' = 'dist = 3' + 'dist = 2' + 'dist = 1' + 'dist = 0'.
    """
    for i in range(3, dist + 1):
        way[i % 3] = way[(i - 1) % 3] + way[(i - 2) % 3] + way[(i - 3) % 3]
    return way[dist % 3]


if __name__ == '__main__':
    dist = 4
    print(wayToCoverDist(dist))
