"""Ways to Cover a Distance
Problem:
        Given a distance ‘dist’, count total number of ways to cover the distance with 1, 2 and 3 steps. 
Example:
    Input: n = 3
    Output: 4
    Explanation: Below are the four ways.
        1 step + 1 step + 1 step
        1 step + 2 step
        2 step + 1 step
        3 step
Refer to:
    1. https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
    Time Complexity: O(n), where `n` is the distance.
    Space Complexity: O(1)
Created by JSheng <jasonhuang0124@gmail.com>"""


def wayToCoverDist(dist):
    way = [0] * 3

    """
    Initialize base values. There is one way({1}) to cover 0 and 1 distances 
    and two ways({1, 1} or {2}) to cover 2 distance.
    """
    way[0] = 1
    way[1] = 1
    way[2] = 2

    """Bottom-up approach???"""
    for i in range(3, dist + 1):
        way[i % 3] = way[(i - 1) % 3] + way[(i - 2) % 3] + way[(i - 3) % 3]
        print('way:', way)
    return way[dist % 3]


if __name__ == '__main__':
    dist = 4
    print(wayToCoverDist(dist))
