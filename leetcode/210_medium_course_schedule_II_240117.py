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
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Dic?
        https://leetcode.com/problems/course-schedule-ii/solutions/4284339/python-beginner-friendly-o-v-e/
        """
        preReq = defaultdict(list)

        for c,pr in prerequisites:
            preReq[c].append(pr)
        
        res = []

        visit, cycle = set(), set()

        def dfs(c):
            # terminating case
            if c in cycle:
                return False
            
            if c in visit:
                return True
            
            cycle.add(c)
            for pr in preReq[c]:
                if dfs(pr) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return res
        """Mine."""
        ans = []
        for i in range(numCourses):
            ans.append(i)
        if len(prerequisites) == 0:
            return ans
        pre_dic = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in pre_dic:
                pre_dic[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                pre_dic[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(numCourses):
            if i in pre_dic:
                

        return ans
    def findRoot(self, pre_dic, target):
        if target in pre_dic:
            self.findRoot(pre_dic, target)

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
