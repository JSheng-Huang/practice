"""LeetCode#2482(Medium) Difference Between Ones and Zeros in Row and Column
Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
Problem:
        You are given a 0-indexed m x n binary matrix grid.
        A 0-indexed m x n difference matrix diff is created with the following 
    procedure:
            Let the number of ones in the ith row be `onesRowi`.
            Let the number of ones in the jth column be `onesColj`.
            Let the number of zeros in the ith row be ``zerosRowi``.
            Let the number of zeros in the jth column be `zerosColj`.
            diff[i][j] = `onesRowi` + `onesColj` - `zerosRowi` - `zerosColj`
        Return the difference matrix diff.
Example:
    #1:
      Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
      Output: [[0,0,4],[0,0,4],[-2,-2,2]]
      Explanation:
            - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
            - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
            - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
            - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
            - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
            - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
            - diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
            - diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
            - diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2
    #2:
      Input: grid = [[1,1,1],[1,1,1]]
      Output: [[5,5,5],[5,5,5]]
      Explanation:
            - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
            - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
            - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
            - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
            - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
            - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5
Constraints: 
    #1. m == grid.length
    #2. n == grid[i].length
    #3. 1 <= m, n <= 105
    #4. 1 <= m * n <= 105
    #5. grid[i][j] is either 0 or 1.
Refer to: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/solutions/4401850/really-simple-3-step-python-solution-o-m-n-time-complexity-o-1-space-complexity/
    Time Complexity: O(m * n).
    Space Complexity: O(1).
    Explanation:
        That this is a `O(1)` space complexity solution because we don't count 
    the space used up by the output `diff` matrix.
Date: 231214.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """Brute Force(Mine): Too slow, but pass."""
        sum_row = []
        sum_col = []
        grid_width = len(grid)
        grid_length = len(grid[0])
        sum_width_length = grid_width + grid_length - 1
        res = []
        for i in range(grid_width):
            tmp = 0
            for j in range(grid_length):
                tmp += grid[i][j]
            sum_row.append(tmp)
        for i in range(grid_length):
            tmp = 0
            for j in range(grid_width):
                tmp += grid[j][i]
            sum_col.append(tmp)
        for i in range(grid_width):
            tmp = []
            for j in range(grid_length):
                """
                `-1`: Duplicated.
                """
                cur = (sum_row[i] + sum_col[j]) - \
                    (sum_width_length - sum_row[i] - sum_col[j]) - 1
                tmp.append(cur)
            res.append(tmp)
        return res

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Its concept is similar to mine, but it's more efficient.
        """
        row_len = len(grid)
        col_len = len(grid[0])
        diff = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for r in range(row_len):
            """
            Compare to mine, it skips anther looping by using a built-in function and count `diff` by only considering rows first.
            """
            row_one_cnt = sum(grid[r])
            row_zero_cnt = col_len - row_one_cnt
            diff[r] = [(row_one_cnt - row_zero_cnt)] * col_len
        for c in range(col_len):
            col_one_cnt = 0
            for r in range(row_len):
                col_one_cnt += grid[r][c]
            col_zero_cnt = row_len - col_one_cnt

            """
            Compare to mine, it combine the counting of `diff` into the second 
            loop, because `diff` here has already stored the result of only 
            considering rows.
            """
            for r in range(row_len):
                diff[r][c] += (col_one_cnt - col_zero_cnt)
        return diff


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[[0,0,4],[0,0,4],[-2,-2,2]]`."""
    print(qwe.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))

    """Should return `[[5,5,5],[5,5,5]]`."""
    print(qwe.onesMinusZeros([[1, 1, 1], [1, 1, 1]]))
