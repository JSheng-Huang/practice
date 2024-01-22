"""LeetCode#210(Medium) Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Problem:
        There are a total of numCourses courses you have to take, labeled from 
    0 to numCourses - 1. You are given an array prerequisites where 
    prerequisites[i] = [ai, bi] indicates that you must take course bi first if 
    you want to take course ai.
        For example, the pair [0, 1], indicates that to take course 0 you have 
    to first take course 1.
        Return the ordering of courses you should take to finish all courses. 
    If there are many valid answers, return any of them. If it is impossible to 
    finish all courses, return an empty array.
Example:
    #1:
      Input: numCourses = 2, prerequisites = [[1,0]]
      Output: [0,1]
      Explanation: 
            There are a total of 2 courses to take. To take course 1 you should 
        have finished course 0. So the correct course order is [0,1].
    #2:
      Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
      Output: [0,2,1,3]
      Explanation: 
            There are a total of 4 courses to take. To take course 3 you should 
        have finished both courses 1 and 2. Both courses 1 and 2 should be 
        taken after you finished course 0.
            So one correct course order is [0,1,2,3]. Another correct ordering 
        is [0,2,1,3].
    #3:
      Input: numCourses = 1, prerequisites = []
      Output: [0]
Constraints: 
    #1. 1 <= numCourses <= 2000
    #2. 0 <= prerequisites.length <= numCourses * (numCourses - 1)
    #3. prerequisites[i].length == 2
    #4. 0 <= ai, bi < numCourses
    #5. ai != bi
    #6. All the pairs [ai, bi] are distinct.
Refer to: 
Date: 240117.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/course-schedule-ii/solutions/4284339/python-beginner-friendly-o-v-e/
        """
        """
        Intuition
        The problem is asking for the order in which courses can be taken given a list of prerequisites.
        We can model the problem as a directed graph, where nodes represent courses and directed edges represent prerequisites.
        The goal is to find a valid topological ordering of the graph.
        Approach
        We can use a depth-first search (DFS) based approach to find a valid topological ordering.

        Create a dictionary (preReq) to represent the directed edges between courses and their prerequisites.
        Initialize an empty list (res) to store the final result, a set (visit) to keep track of visited nodes, and a set (cycle) to detect cycles during the DFS traversal.
        Define a DFS function that takes a course as an argument.
        Check if the course is in the cycle set. If true, there is a cycle, and return False.
        Check if the course is in the visit set. If true, the course is already processed, return True.
        Add the course to the cycle set to mark it as visited.
        Recursively call the DFS function for each prerequisite of the current course.
        Remove the course from the cycle set (backtrack) and add it to the visit set.
        Append the course to the result list.
        Return True.
        Iterate through all courses and call the DFS function for each course.
        If the DFS function returns False, there is a cycle, and the result is not possible, return an empty list.
        Return the result list as the valid topological ordering.
        Complexity
        Time complexity:
        O(N + E), where N is the number of courses and E is the number of prerequisites. The DFS traversal visits each course once and each prerequisite once.

        Space complexity:
        O(N + E) for the graph representation and recursion stack. The preReq dictionary stores the graph, and the visit and cycle sets store information during DFS.
        """
        pre_req = {}
        for i, j in prerequisites:
            if i not in pre_req:
                pre_req[i] = []
            pre_req[i].append(j)
        res = []
        visit, cycle = set(), set()
        for c in range(numCourses):
            if self.dfs(c, pre_req, cycle, visit, res) == False:
                return []
        return res

    def dfs(self, c, pre_req, cycle, visit, res):
        # terminating case
        if c in cycle:
            return False
        if c in visit:
            return True
        cycle.add(c)
        if pre_req.get(c):
            for pr in pre_req[c]:
                if self.dfs(pr, pre_req, cycle, visit, res) == False:
                    return False
        cycle.remove(c)
        visit.add(c)
        res.append(c)
        return True


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[0,1]`."""
    print(qwe.findOrder(2, [[1, 0]]))

    """Should return `[0,2,1,3]`."""
    print(qwe.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    """Should return `[0]`."""
    print(qwe.findOrder(1, []))

    """Should return `[]`."""
    print(qwe.findOrder(2, [[0, 1], [1, 0]]))

    """Should return `[]`."""
    print(qwe.findOrder(3, [[1, 0], [0, 2], [2, 1]]))
