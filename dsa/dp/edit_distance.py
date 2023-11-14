"""Longest Increasing Subsequence
Problem:
        Given two strings `str1` and `str2` of length m and n respectively and 
    below operations that can be performed on `str1`. Find the minimum number 
    of edits(operations) to convert ‘str1‘ into ‘str2‘.  
    Operation 1(insert): Insert any character before or after any index of 
    `str1`.
    Operation 2(remove): Remove a character of `str1.`
    Operation 3(replace): Replace a character at any index of `str1` with some 
    other character.
Example:
    Input: `str1 = 'sunday'`, `str2 = 'saturday'`.
    Output: `3`
    Explanation: Last three and first characters are same. We basically need to 
    convert "un" to "atur".  This can be done using below three operations. 
    Replace "n" with "r", insert "t", insert "a".
Refer to:
    1. https://www.geeksforgeeks.org/edit-distance-dp-5/
    Time Complexity: O(m x n), where `m` and `n` are lengths of `str1` and 
    `str2`.
    Space Complexity: O(n), where `n` is length of `str2`.
Created by JSheng <jasonhuang0124@gmail.com>"""


def editDistance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    curr = [i for i in range(str2_len + 1)]
    prev = 0

    # Loop through the rows of the dynamic programming matrix
    for i in range(1, str1_len + 1):
        prev = curr[0]
        curr[0] = i
        for j in range(1, str2_len + 1):
            temp = curr[j]
            if i == 3 and j == 2:
                print(curr)
                print('temp', temp)
            if i == 3 and j == 3:
                print('before', curr)
                print('current j:', j)
                print('prev: ', prev)
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev
            else:
                curr[j] = 1 + min(prev, curr[j - 1], curr[j])
            prev = temp
            if i == 3 and j == 3:
                print('in:', curr)
                print('===')
    """
    Values in `curr` mean if `str1` is only considered from `0` to
    ???
    """
    return curr[str2_len]


if __name__ == "__main__":
    str1 = 'hit'
    str2 = 'kitty'

    """The answer is 3 when `str1 = 'hit'` and `str2 = 'kitty'`."""
    print('Edit distance is:', editDistance(str1, str2))
