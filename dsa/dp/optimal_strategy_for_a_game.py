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
    Time Complexity: O(n ^ 2).
    Space Complexity: O(n ^ 2). As a 2-D table is used for storing states.
Created by JSheng <jasonhuang0124@gmail.com>"""


def optimalStrategyOfGame(arr, n):
    table = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            """
            Example:
                [8, 15, 11, 22]
                [0, 15, 15, 18]
                [0,  0,  3,  7]
                [0,  0,  0,  7]
            If `gap` == 0: Only one option.
            If `gap` == 1: Two options, so pick the larger one.
            e.g.:
                `j` == 1: [ 8, 15], pick `15`.
                `j` == 2: [15,  3], pick `15`.
                `j` == 3: [ 3,  7], pick `7`.
            """
            if gap < 2:
                x = 0
                y = 0
                z = 0
            else:
                """
                If `gap` == 2: Three options, so pick the larger "combination" 
                from the previous result.
                e.g.:
                `j` == 2: [ 8, 15, 3], pick `8` and `3`, coz the opponent would 
                pick `15` while options = [15, 3], so the sum user gets = 11.
                `j` == 3: [15,  3, 7], pick `15` and `3`, coz the opponent 
                would pick `7` while options = [3, 7], so the sum user gets = 
                18.
                If `gap` == 3: Three options, so pick the larger "combination" 
                from the previous result.
                e.g.:
                `j` == 3: [15, 15, 7], pick `15` and `7`, coz the opponent 
                would pick `15` while options = [15, 7], so the sum user gets = 
                22.
                """
                x = table[i + 2][j]
                y = table[i + 1][j - 1]
                z = table[i][j - 2]
            """
            If `arr = [x, y, z]`, you could only decide to pick `x` or `z', and the opponent would leave the smaller one of the other to you.
            """
            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    return table[0][n - 1]


if __name__ == '__main__':
    arr = [8, 15, 3, 7]
    n = len(arr)
    print(optimalStrategyOfGame(arr, n))
