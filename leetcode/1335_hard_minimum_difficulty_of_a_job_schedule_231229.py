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
        Time complexity: O(d * n)
        Space complexity: O(n)
        """
        """
        To calculate today[i], we only use yesterday[i - 1]
        or more precisely: When calculating today[i], we only need to store today[:i + 1] and yesterday[i:].
        """
        n = len(jobDifficulty)
        if d > n:
            return -1
        """
        `today` is the DP array for the current day.
        `today[i]` is the total difficulty of the optimal solution for jobs from `0` to `i` after each day.
        Solution for day 0 is just the running maximum.
        """
        """Author."""
        # today = deepcopy(jobDifficulty)

        today = jobDifficulty.copy()

        """
        Input: [11, 111, 22, 222, 33, 333, 44, 444]
        Output: [11, 111, 111, 222, 222, 333, 333, 444]
        """
        for i in range(1, n):
            today[i] = max(today[i], today[i - 1])
        for cur_day in range(1, d):
            """Author:
            # The checkpoints stack contains all previous jobs index i
            # where the optimal solution for today[i] has jobs[i] as
            # the most difficult in the last day (`cur_day`).

            # The idea is, starting with a solution that has only jobs[cur_job]
            # for the last day (i.e today), we will try to include previous
            # jobs to find a smaller total difficulty. Instead of considering
            # all previous jobs, we maintain a checkpoint list of all previous
            # jobs that may improve the current solution.

            # For `last_checkpoint` < `cur_job`,
            # if jobDifficulty[last_checkpoint] < jobDifficulty[cur_job],
            # then we can consider including jobs[last_checkpoint] in "the
            # last day of the current solution for today[cur_job]".
            # Here the difficulty of the last day is unchanged but the total
            # difficulty might change, so we evaluate the new solution then
            # move to the previous checkpoint. How to evaluate the solution
            # is will be explained along with the code.

            # Otherwise, if jobDifficulty[last_checkpoint] > jobDifficulty[cur_job],
            # then the optimal solution for today[cur_job] can either include or not
            # include job[last_checkpoint]:
            #     - if it does include, then the solution for today[cur_job] will
            #     just be an extension of the solution for today[last_checkpoint]
            #     (extend the last day of solution for today[last_checkpoint] with
            #     jobs `last_checkpoint + 1` -> `cur_job`). This is because solution
            #     for today[last_checkpoint] is optimal and has jobs[last_checkpoint]
            #     as the most difficult in the last day. So any other solution that
            #     "has jobs[last_checkpoint] as the most difficult in the last day"
            #     cannot do better than today[cur_job].
            #     Thus today[cur_job] = today[last_checkpoint] is optimal.
            #     - if it doesn't include, then the current solution for today[cur_job]
            #     is already the optimal one.

            # For example,
            # when evaluating today[27] and the checkpoints are [..., 5, 13, 20]
            #
            #     jobs            ...     5   ...     13  ...     20  ...     27
            #     difficulty      (any)   21  (< 17)  17  (< 13)  13  (< 13)  19
            #     today           ...     x   ...     y   ...     z   ...     ?
            #
            # we can consider previous jobs[20] and then jobs[13] (which has smaller
            # difficulty) and uses `y` and `z` (i.e. optimal solution for today[20] and today[13])
            # to update today[27].
            #
            # Until we encounter jobs[5], now whether the optimal solution for today[27]
            # includes jobs[5] or not, we know that there's no use in considering further
            # previous checkpoints. So we evaluate this last candidate using `x` then stop.

            # Thus we maintain the list `checkpoints` such that, for i in `checkpoints`
            #     - `jobDifficulty[i]` is monotonically decreasing
            #         => `checkpoints` is a monotonic decreasing stack of jobs with
            #         respected to their difficulty
            #     - and the optimal solution for today[i] has jobs[i] as
            #     the most difficult of the last day (`cur_day`).
            """
            checkpoints = []
            day_left = d - cur_day - 1

            """
            Cache the value of the last index(yesterday), it means the solution 
            when we only consider from `0` to `cur_day - 1`, and that's why the 
            outer loop should start from `1`.
            """
            cache = today[cur_day - 1]

            """Author:
            # for `cur_day`, one can only works on jobs[i : n - day_left - 1]
            # (so that `cur_day - 1` previous days and `day_left` remaining days
            # each has at least 1 job)
            """
            """My wording:
            In the inner loop, we only consider days from `cur_day` to `n - 
            day_left`.
            For `cur[:cur_day]`: We have found the best solution in that 
            interval.
            For `cur[n - day_left:]`: We have to keep these remaining days for 
            1 job per day at least.
            """
            for cur_job in range(cur_day, n - day_left):
                cur_difficulty = jobDifficulty[cur_job]

                """???Author:
                # caching the solution of yesterday at cur_job
                # so it can be used for today[cur_job + 1] in the next iteration
                """
                tmp = today[cur_job]

                """The base case is only works on `jobs[cur_job]` for today."""
                today[cur_job] = cur_difficulty + cache

                # update cache to use for the next job
                cache = tmp

                # Started with only `cur_job` for today (as mentioned above),
                # maintain the following loop invariance:
                #     the current solution for today[cur_job] has jobs[cur_job]
                #     as the hardest jobs of the last day,
                # and gradually trying to extend to previous jobs (checkpoints).

                # The loop ends either when it exhausts
                # or when we can no longer maintain the invariance.
                while checkpoints:
                    """Author:
                    If the last job in the stack(`last_checkpoint`) is less 
                    difficult than `cur_job`, then we can have the option to 
                    extend the solution at today[last_checkpoint] with all the 
                    jobs upto `cur_job`.
                    Because the solution at today[last_checkpoint] has 
                    `last_checkpoint` as the most difficult, so after extend to 
                    `cur_job`, the new hardest is `cur_job`, thus the total 
                    diff is increased by `jobDifficulty[cur_job] - jobDifficulty
                    [last_checkpoint]`.
                    Choose to extend or not by comparing `today[cur_job]` and `today[last_checkpoint] + cur_difficulty - jobDifficulty[last_checkpoint]`:
                        `today[cur_job]`: 
                            Not to extend, so it means to use a single day to 
                        do `cur_job`.
                        `today[last_checkpoint] + cur_difficulty - jobDifficulty[last_checkpoint]`: 
                            To extend, so it means `cur_job` is the most difficulty of jobDifficulty[`last_checkpoint`]use a single day to 
                        do the job.
                    """
                    if jobDifficulty[checkpoints[-1]] < cur_difficulty:
                        last_checkpoint = checkpoints.pop()
                        print('cur_job', cur_job)
                        print('today[cur_job]', today[cur_job])
                        print('today[last_checkpoint]', today[last_checkpoint])
                        print(today[last_checkpoint] + cur_difficulty -
                              jobDifficulty[last_checkpoint])
                        print()
                        today[cur_job] = min(
                            today[cur_job], today[last_checkpoint] + cur_difficulty - jobDifficulty[last_checkpoint])
                    else:
                        """Author:
                        # else, this is the last checkpoint that we can consider (as discussed before).
                        # After consider this one, we will have found the optimal solution for today[cur_job]
                        # If we find a better solution for today[cur_job] then this solution
                        # has `cur_job` as the hardest of the last day (i.e. the current day)
                        # (this is the loop invariance), so we add it to the checkpoints.
                        """
                        """My wording:
                        
                        """
                        if today[cur_job] < today[checkpoints[-1]]:
                            checkpoints.append(cur_job)
                        else:
                            # else we extend the solution at today[checkpoints[-1]] to `cur_job`,
                            # meaning jobs[checkpoints[-1]] is the hardest of solution for today[cur_job]
                            today[cur_job] = today[checkpoints[-1]]
                        break
                else:
                    """
                    If there is no checkpoints left then the solution for 
                    today[cur_job] that we just found has `cur_job` as the most difficult of the last day(the loop invariance).
                    """
                    checkpoints.append(cur_job)
                # Each iteration of the while loop we either add or remove a checkpoint.
                # Since each job is added and/or removed at most once for each day,
                # the time complexity is $$O(d*n)$$ instead of $$O(d*n*n)$$
            # print(today)
        return today[-1]


if __name__ == '__main__':
    qwe = Solution()

    """Should return `7`."""
    # print(qwe.minDifficulty([6, 5, 4, 3, 2, 1], 2))

    """Should return `-1`."""
    # print(qwe.minDifficulty([9, 9, 9], 4))

    """Should return `3`."""
    # print(qwe.minDifficulty([1, 1, 1], 3))

    """Should return `15`."""
    # print(qwe.minDifficulty([7, 1, 7, 1, 7, 1], 3))

    """Should return `843`."""
    # print(qwe.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))

    """Should return `1803`."""
    print(qwe.minDifficulty([186, 398, 479, 206, 885, 423,
          805, 112, 925, 656, 16, 932, 740, 292, 671, 360], 4))
