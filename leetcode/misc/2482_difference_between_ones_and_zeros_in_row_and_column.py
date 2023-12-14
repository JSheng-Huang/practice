"""LeetCode#2482(Medium) Difference Between Ones and Zeros in Row and Column
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
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
Note: N/A.
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
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        sum_row = []
        sum_col = []
        sum_width_length = len(grid) + len(grid[0])
        res = []
        for i in range(len(grid)):
            tmp = 0
            for j in range(len(grid[0])):
                tmp += grid[i][j]
            sum_row.append(tmp)
        for i in range(len(grid[0])):
            tmp = 0
            for j in range(len(grid)):
                tmp += grid[j][i]
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp.append(- 1)
                else:
                    tmp.append(- 1)
            res.append(tmp)
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Return `[[0,0,4],[0,0,4],[-2,-2,2]]`."""
    print(qwe.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))

    # """Return `[[5,5,5],[5,5,5]]`."""
    # print(qwe.onesMinusZeros([[1, 1, 1], [1, 1, 1]]))
