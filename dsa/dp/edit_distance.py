"""Longest Increasing Subsequence
Problem:
        Given two strings `str1` and `str2` of length m and n respectively and 
    below operations that can be performed on `str1`. Find the minimum number 
    of edits(operations) to convert ‘str1‘ into ‘str2‘.  
    Operation 1(insert): Insert any character before or after any index of 
    `str1`.
    Operation 2(remove): Remove a character of `str1.`
    Operation 3(replace): Replace a character at any index of `str1` with some other character.
Example:
    Input: `str1 = 'sunday'`, `str2 = 'saturday'`.
    Output: `3`
    Explanation: Last three and first characters are same. We basically need to convert "un" to "atur".  This can be done using below three operations. Replace "n" with "r", insert "t", insert "a".
Refer to:
    1. https://www.geeksforgeeks.org/edit-distance-dp-5/
    Time Complexity: O(m x n) where `m` and `n` are lengths of `str1` and 
    `str2`.
    Space Complexity: O(n), where `n` is length of `str2`.
Created by JSheng <jasonhuang0124@gmail.com>"""


def editDistance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    # Initialize a list to store the current row
    curr = [0] * (str2_len + 1)

    # Initialize the first row with values from 0 to n
    for j in range(str2_len + 1):
        curr[j] = j

    # Initialize a variable to store the previous value
    previous = 0

    # Loop through the rows of the dynamic programming matrix
    for i in range(1, str1_len + 1):
        # Store the current value at the beginning of the row
        previous = curr[0]
        curr[0] = i

        # Loop through the columns of the dynamic programming matrix
        for j in range(1, str2_len + 1):
            # Store the current value in a temporary variable
            temp = curr[j]

            # Check if the characters at the current positions in str1 and str2 are the same
            if str1[i - 1] == str2[j - 1]:
                curr[j] = previous
            else:
                # Update the current cell with the minimum of the three adjacent cells
                curr[j] = 1 + min(previous, curr[j - 1], curr[j])

            # Update the previous variable with the temporary value
            previous = temp

    # The value in the last cell represents the minimum number of operations
    return curr[str2_len]


if __name__ == "__main__":
    str1 = 'sit'
    str2 = 'kiit'

    """The answer is 2 when `str1 = 'sit'` and `str2 = 'kiit'`."""
    print('Edit distance is:', editDistance(str1, str2))
