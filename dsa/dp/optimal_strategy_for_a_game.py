"""Optimal Strategy for a Game
Problem:
        Consider a row of N coins of values V1 . . . Vn, where N is even. We 
    play a game against an opponent by alternating turns. In each turn, a 
    player selects either the first or last coin from the row, removes it from 
    the row permanently, and receives the value of the coin. Determine the 
    maximum possible amount of money we can definitely win if we move first.
    Note: The opponent is as clever as the user. 
Refer to:
    1. https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
    Time Complexity:  O(n^2).
    Space Complexity: O(n^2). As a 2-D table is used for storing states.
Created by JSheng <jasonhuang0124@gmail.com>"""


def optimalStrategyOfGame(arr, n):
    table = [[0 for _ in range(n)] for _ in range(n)]

    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # (similar to http://goo.gl / PQqoS),
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            # Here x is value of F(i + 2, j),
            # y is F(i + 1, j-1) and z is
            # F(i, j-2) in above recursive
            # formula
            x = 0
            if ((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if ((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if (i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]


if __name__ == '__main__':
    arr1 = [8, 15, 3, 7]
    n = len(arr1)
    print(optimalStrategyOfGame(arr1, n))

    arr2 = [2, 2, 2, 2]
    n = len(arr2)
    print(optimalStrategyOfGame(arr2, n))

    arr3 = [20, 30, 2, 2, 2, 10]
    n = len(arr3)
    print(optimalStrategyOfGame(arr3, n))
