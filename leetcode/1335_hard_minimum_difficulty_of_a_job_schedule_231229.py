"""LeetCode#1335(Hard) Minimum Difficulty of a Job Schedule
Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/?envType=daily-question&envId=2023-12-29
Problem:
        You want to schedule a list of jobs in d days. Jobs are dependent (i.e 
    To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
        You have to finish at least one task every day. The difficulty of a job 
    schedule is the sum of difficulties of each day of the d days. The 
    difficulty of a day is the maximum difficulty of a job done on that day.
        You are given an integer array jobDifficulty and an integer d. The 
    difficulty of the ith job is jobDifficulty[i].
        Return the minimum difficulty of a job schedule. If you cannot find a 
    schedule for the jobs return -1.
Example:
    #1:
      Input: jobDifficulty = [6,5,4,3,2,1], d = 2
      Output: 7
      Explanation: 
            First day you can finish the first 5 jobs, total difficulty = 6.
            Second day you can finish the last job, total difficulty = 1.
            The difficulty of the schedule = 6 + 1 = 7 
    #2:
      Input: jobDifficulty = [9,9,9], d = 4
      Output: -1
      Explanation: 
            If you finish a job per day you will still have a free day. you 
        cannot find a schedule for the given jobs.
    #3:
      Input: jobDifficulty = [1,1,1], d = 3
      Output: 3
      Explanation: The schedule is one job per day. total difficulty will be 3.
Constraints: 
    #1. 1 <= jobDifficulty.length <= 300
    #2. 0 <= jobDifficulty[i] <= 1000
    #3. 1 <= d <= 10
Refer to: ???
Date: 231229.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/solutions/2812707/most-efficient-solution-with-detailed-comments-o-d-n-100-o-n-98-97/?envType=daily-question&envId=2023-12-29
        """
        """
        Complexity
        Time complexity: O(d∗n)O(d * n)O(d∗n)
        Space complexity: O(n)O(n)O(n)
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        today = [None] * n
        yesterday = [jobDifficulty[0]] + [None] * (n - 1)
        # Solution for day 0 is just the running maximum
        for i in range(1, n):
            yesterday[i] = max(yesterday[i - 1], jobDifficulty[i])

        for day in range(1, d):
            # stack contains all index i where today[i] has a solution with jobDifficulty[i]
            # as the biggest
            stack = []
            for i in range(day, n):
                today[i] = yesterday[i - 1] + jobDifficulty[i]
                # Each iteration of the while loop we either add or remove an item.
                # Since each job is added and/or removed at most once for each day,
                # the time complexity is still O(d*n)
                while stack:
                    # If the last job in the stack is less difficult than job i
                    # then we can have the option to add job j+1 -> i to today[i]
                    # Because solution at today[j] has jobDifficulty[j] as the biggest,
                    # so after add job j+1 -> i, the new biggest is diff[i],
                    # thus the total jobDifficulty is inceaseed by (jobDifficulty[i] + jobDifficulty[j])
                    if jobDifficulty[stack[-1]] < jobDifficulty[i]:
                        j = stack.pop()
                        today[i] = min(today[i], today[j] - diff[j] + diff[i])
                    else:
                        # If we find a better solution at job i
                        # then in this solution jobDifficulty[i] is the biggest.
                        # add it to the stack
                        if today[i] < today[stack[-1]]:
                            stack.append(i)
                        # else job i is a part of the solution at today[stack[-1]]
                        else:
                            today[i] = today[stack[-1]]
                        break
                else:
                    # If stack is empty then of course we have a new solution at job i
                    stack.append(i)

            yesterday = today.copy()

        return yesterday[-1]


if __name__ == '__main__':
    qwe = Solution()

    """Should return `7`."""
    print(qwe.minDifficulty([6, 5, 4, 3, 2, 1], 2))

    """Should return `-1`."""
    print(qwe.minDifficulty([9, 9, 9], 4))

    """Should return `3`."""
    print(qwe.minDifficulty([1, 1, 1], 3))

    """Should return `15`."""
    print(qwe.minDifficulty([7, 1, 7, 1, 7, 1], 3))

    """Should return `843`."""
    print(qwe.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))
