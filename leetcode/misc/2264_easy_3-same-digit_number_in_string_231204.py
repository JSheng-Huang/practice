"""LeetCode#2264(Easy) Largest 3-Same-Digit Number in String
Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2023-12-04
Problem:
        You are given a string num representing a large integer. An integer is 
    good if it meets the following conditions:
            #1. It is a substring of num with length 3.
            #2. It consists of only one unique digit.
        Return the maximum good integer as a string or an empty string "" if no 
    such integer exists.
Note:
    #1. A substring is a contiguous sequence of characters within a string.
    #2. There may be leading zeroes in num or a good integer.
Example:
    #1:
      Input: num = "6777133339"
      Output: "777"
      Explanation: 
            There are two distinct good integers: "777" and "333". "777" is the 
        largest, so we return "777".
    #2:
      Input: num = "2300019"
      Output: "000"
      Explanation: "000" is the only good integer.
    #3:
      Input: num = "42352338"
      Output: ""
      Explanation: 
            No substring of length 3 consists of only one unique digit. 
        Therefore, there are no good integers.
Constraints: 
    #1. 3 <= num.length <= 1000.
    #2. num only consists of digits.
Refer to: Myself.
    Time Complexity: O(n)?
    Space Complexity: O(1)?
    Explanation: N/A.
Date: 231204.
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_len = len(num)
        ans = -1
        for i in range(num_len - 2):
            if num[i + 1] == num[i] and num[i + 2] == num[i]:
                tmp = int(num[i:i+3])
                if tmp > int(ans):
                    ans = num[i:i+3]
        if ans != -1:
            return ans
        else:
            return ''


if __name__ == '__main__':
    qwe = Solution()

    """Return `777`."""
    print(qwe.largestGoodInteger('6777133339'))

    """Return `000`."""
    print(qwe.largestGoodInteger('2300019'))

    """Return ``."""
    print(qwe.largestGoodInteger('42352338'))
