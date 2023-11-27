"""0-1 Knapsack Problem
Problem:
        Given N items where each item has some weight and profit associated 
    with it and also given a bag with capacity W, [i.e., the bag can hold at 
    most W weight in it]. The task is to put the items into the bag such that 
    the sum of profits associated with them is the maximum possible. 
Note: 
        The constraint here is we can either put an item completely into the 
    bag or cannot put it at all [It is not possible to put a part of an item 
    into the bag].
Refer to: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
Time Complexity: O(N * W). As redundant calculations of states are avoided.
Space Complexity: O(W) As we are using a 1-D array instead of a 2-D array.
Created by JSheng <jasonhuang0124@gmail.com>"""


def knapSack(weight_limit, wt, val, n):
    dp = [0 for _ in range(weight_limit + 1)]
    for i in range(1, n + 1):
        for w in range(weight_limit, 0, -1):
            """The pack is affordable for the weight of the current item."""
            if w >= wt[i - 1]:
                """
                `dp[w]`(before updating): Do not take the current item, which 
                means just take the previous result which only takes `wt[0:i]` 
                into account.`dp[w - wt[i - 1]]`: Get the maximum profit from 
                the current weight limit which minus the weight of the current 
                item, which means the maximum profit that does not take the 
                value of the current item into account.
                `val[i - 1]`: The profit of the current item.
                """
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
    return dp[weight_limit]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    weight_limit = 50
    n = len(profit)
    print(knapSack(weight_limit, weight, profit, n))
