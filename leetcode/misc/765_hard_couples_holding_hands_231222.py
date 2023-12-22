"""LeetCode#765(Hard) Couples Holding Hands
Link: https://leetcode.com/problems/couples-holding-hands/
Problem:
        There are n couples sitting in 2n seats arranged in a row and want to 
    hold hands.
        The people and seats are represented by an integer array row where row
    [i] is the ID of the person sitting in the ith seat. The couples are 
    numbered in order, the first couple being (0, 1), the second couple being 
    (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
        Return the minimum number of swaps so that every couple is sitting side 
    by side. A swap consists of choosing any two people, then they stand up and 
    switch seats.
Example:
    #1:
      Input: row = [0,2,1,3]
      Output: 1
      Explanation: 
            We only need to swap the second (row[1]) and third (row[2]) person.
    #2:
      Input: row = [3,2,0,1]
      Output: 0
      Explanation: All couples are already seated side by side.
Constraints: 
    #1. 2n == row.length
    #2. 2 <= n <= 30
    #3. n is even.
    #4. 0 <= row[i] < 2n
    #5. All the elements of row are unique.
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Date: 231222.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List, Optional


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """row[n] and row[n + 1] should be couple"""
        res = 0
        n = len(row)
        for i in range(0, n - 2, 2):
            print(i)
            abs_diff = abs(row[i] - row[i + 1])
            if abs_diff != 1:
                res += 1
                for j in range(i + 2, n):
                    abs_diff = abs(row[i] - row[j])
                    if abs_diff == 1:
                        row[i + 1], row[j] = row[j], row[i + 1]
                        break
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Should return `1`."""
    # print(qwe.minSwapsCouples([0, 2, 1, 3]))

    """Should return `0`."""
    # print(qwe.minSwapsCouples([3, 2, 0, 1]))

    """Should return `3`."""
    print(qwe.minSwapsCouples([6, 2, 1, 7, 4, 5, 3, 8, 0, 9]))
