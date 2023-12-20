"""LeetCode#2076(Hard) Process Restricted Friend Requests
Link: https://leetcode.com/problems/process-restricted-friend-requests/
Problem:
        You are given an integer n indicating the number of people in a 
    network. Each person is labeled from 0 to n - 1.
        You are also given a 0-indexed 2D integer array restrictions, where 
    restrictions[i] = [x_i, y_i] means that person xi and person yi cannot 
    become friends, either directly or indirectly through other people.
        Initially, no one is friends with each other. You are given a list of 
    friend requests as a 0-indexed 2D integer array requests, where requests[j] 
    = [u_j, v_j] is a friend request between person u_j and person v_j.
        A friend request is successful if u_j and v_j can be friends. Each 
    friend request is processed in the given order (i.e., requests[j] occurs 
    before requests[j + 1]), and upon a successful request, u_j and v_j become 
    direct friends for all future friend requests.
        Return a boolean array result, where each result[j] is true if the jth 
    friend request is successful or false if it is not.
Note: 
    If u_j and v_j are already direct friends, the request is still successful.
Example:
    #1:
      Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
      Output: [true,false]
      Explanation:
            Request 0: Person 0 and person 2 can be friends, so they become 
        direct friends. 
            Request 1: Person 2 and person 1 cannot be friends since person 0 
        and person 1 would be indirect friends (1--2--0).
    #2:
      Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
      Output: [true,false]
      Explanation:
            Request 0: Person 1 and person 2 can be friends, so they become 
        direct friends.
            Request 1: Person 0 and person 2 cannot be friends since person 0 
        and person 1 would be indirect friends (0--2--1).
    #3:
      Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],
      [3,1],[3,4]]
      Output: [true,false,true,false]
      Explanation:
            Request 0: Person 0 and person 4 can be friends, so they become 
        direct friends.
            Request 1: Person 1 and person 2 cannot be friends since they are 
        directly restricted.
            Request 2: Person 3 and person 1 can be friends, so they become 
        direct friends.
            Request 3: Person 3 and person 4 cannot be friends since person 0 
        and person 1 would be indirect friends (0--4--3--1).
Constraints: 
    #1. 2 <= n <= 1000
    #2. 0 <= restrictions.length <= 1000
    #3. restrictions[i].length == 2
    #4. 0 <= x_i, y_i <= n - 1
    #5. x_i != y_i
    #6. 1 <= requests.length <= 1000
    #7. requests[j].length == 2
    #8. 0 <= u_j, v_j <= n - 1
    #9. u_j != v_j
Refer to: https://leetcode.com/problems/process-restricted-friend-requests/solutions/4233975/python3-simple-union-find/
Date: 231212.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        self.parent = list(range(n))
        res = []
        for a, b in requests:
            temp = self.parent.copy()
            flag = True
            self.union(a, b)
            for x, y in restrictions:
                """
                Both `x` and `y` have the same root if `a` connects to `b`.
                """
                if self.find(x) == self.find(y):
                    flag = False
                    break
            if flag:
                res.append(True)
            else:
                res.append(False)

                """Reset"""
                self.parent = temp
        return res

    def find(self, a):
        a_cp = a

        """Find the root."""
        while a != self.parent[a]:
            a = self.parent[a]
        """Update the root."""
        if a_cp != a:
            self.parent[a_cp] = a
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
        return


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[true,false]`."""
    # print(qwe.friendRequests(3, [[0, 1]], [[0, 2], [2, 1]]))

    """Should return `[true,false]`."""
    # print(qwe.friendRequests(3, [[0, 1]], [[1, 2], [0, 2]]))

    """Should return `[true,false,true,false]`."""
    print(qwe.friendRequests(5, [[0, 1], [1, 2], [2, 3]], [
          [0, 4], [1, 2], [3, 1], [3, 4]]))

    """
    Should return `[true,false,true,false,false,true,false,true,false,false,false,
    false,false,true,false,false,true,false,false,false,false,false,true,false,
    false,false,false,false]`.
    """
    # print(qwe.friendRequests(8, [[6, 4], [7, 5], [2, 6], [1, 5], [6, 7], [6, 5], [0, 3], [5, 4], [0, 4], [2, 7], [0, 2]], [[6, 3], [0, 2], [0, 5], [0, 3], [6, 4], [2, 4], [1, 0], [
    #       2, 1], [2, 5], [6, 7], [7, 0], [3, 2], [3, 5], [2, 1], [1, 6], [7, 4], [6, 3], [1, 3], [6, 5], [3, 7], [7, 0], [6, 5], [0, 5], [0, 4], [7, 5], [7, 0], [7, 0], [1, 3]]))
