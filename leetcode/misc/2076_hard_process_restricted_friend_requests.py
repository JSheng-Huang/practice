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
Refer to: ???
    Time Complexity: ???
    Space Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        blocked_map = {}
        blocked_list = []
        res = []
        for i in restrictions:
            if blocked_map.get(i[0]):
                blocked_map[i[0]].append(i[1])
            else:
                blocked_map[i[0]] = []
                blocked_map[i[0]].append(i[1])
        for i in requests:
            if blocked_map.get(i[0]):
                if i[1] in blocked_map.get(i[0]) or i[1] in blocked_list:
                    if i[1] not in blocked_list:
                        blocked_list.append(i[1])
                    res.append(False)
            else:
                res.append(True)
        return res


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # Maintain two lists of sets connected_components and banned_by_comps to store the connected components the restrictions of nodes in each connected component. Maintain a dictionary connected_comp_dict to map each node to its connected component. Update them when a new edge is added.
        result = [False for _ in requests]

        connected_components = [{i} for i in range(n)]

        connected_comp_dict = {}
        for i in range(n):
            connected_comp_dict[i] = i
        print(connected_comp_dict)
        banned_by_comps = [set() for i in range(n)]
        for res in restrictions:
            banned_by_comps[res[0]].add(res[1])
            banned_by_comps[res[1]].add(res[0])
        print(banned_by_comps)
        for i, r in enumerate(requests):
            n1, n2 = r[0], r[1]
            c1, c2 = connected_comp_dict[n1], connected_comp_dict[n2]
            if c1 == c2:
                result[i] = True
            else:
                if not connected_components[c1].intersection(banned_by_comps[c2]):
                    connected_components[c1].update(connected_components[c2])
                    banned_by_comps[c1].update(banned_by_comps[c2])
                    for node in connected_components[c2]:
                        connected_comp_dict[node] = c1
                    result[i] = True

        return result


"""https://leetcode.com/problems/process-restricted-friend-requests/solutions/1576965/python3-union-find/"""


class UnionFind:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p: int, halving: bool = True) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt:
            return False
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UnionFind(n)
        print(uf.parent)
        print(uf.rank)
        for u, v in requests:
            uu = uf.find(u)
            vv = uf.find(v)
            for x, y in restrictions:
                xx = uf.find(x)
                yy = uf.find(y)
                if uu == xx and vv == yy or uu == yy and vv == xx:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        uf.union(u, v)
        print(uf.parent)
        print(uf.rank)

        return ans


if __name__ == '__main__':
    qwe = Solution()

    """Return `[true,false]`."""
    print(qwe.friendRequests(3, [[0, 1]], [[0, 2], [2, 1]]))

    """Return `[true,false]`."""
    print(qwe.friendRequests(3, [[0, 1]], [[1, 2], [0, 2]]))

    """Return `[true,false,true,false]`."""
    print(qwe.friendRequests(5, [[0, 1], [1, 2], [2, 3]], [
          [0, 4], [1, 2], [3, 1], [3, 4]]))
