"""LeetCode#1716(Easy) Calculate Money in Leetcode Bank
Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2023-12-06
Problem:
        Hercy wants to save money for his first car. He puts money in the 
    Leetcode bank every day.
        He starts by putting in $1 on Monday, the first day. Every day from 
    Tuesday to Sunday, he will put in $1 more than the day before. On every 
    subsequent Monday, he will put in $1 more than the previous Monday.
        Given n, return the total amount of money he will have in the Leetcode 
    bank at the end of the nth day.
Note: N/A.
Example:
    #1:
      Input: n = 4
      Output: 10
      Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
    #2:
      Input: n = 10
      Output: 37
      Explanation: 
            After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 
        3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
    #3:
      Input: n = 20
      Output: 96
      Explanation: 
            After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 
        3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
Constraints: 1 <= n <= 1000
Refer to: Myself.
Time Complexity: O(1)?
Space Complexity: O(1)?
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def totalMoney(self, n: int) -> int:
        if n < 7:
            if n == 1:
                return 1
            else:
                return int((1 + n) * n / 2)
        else:
            week = n // 7
            res = n % 7
            multiplier = week * (week - 1) / 2
            week_sum = 28 * week + 7 * multiplier
            if res == 0:
                return int(week_sum)
            else:
                res_bgn = 1 * week + 1
                res_sum = (res_bgn + res_bgn + res - 1) * res / 2
            return int(week_sum + res_sum)


if __name__ == '__main__':
    qwe = Solution()
    """Return `135`."""
    print(qwe.totalMoney(26))
