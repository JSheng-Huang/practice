"""LeetCode#57(Medium) Insert Interval
Link: https://leetcode.com/problems/insert-interval/
Problem:
        You are given an array of non-overlapping intervals intervals where 
    intervals[i] = [start_i, end_i] represent the start and the end of the ith 
    interval and intervals is sorted in ascending order by start_i. You are 
    also given an interval newInterval = [start, end] that represents the start 
    and end of another interval.
        Insert new_Interval into intervals such that intervals is still sorted 
    in ascending order by start_i and intervals still does not have any 
    overlapping intervals (merge overlapping intervals if necessary).
        Return intervals after the insertion.
Example:
    #1:
      Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
      Output: [[1,5],[6,9]]
    #2:
      Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
      Output: [[1,2],[3,10],[12,16]]
      Explanation: 
            Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Constraints: 
    #1. 0 <= intervals.length <= 104
    #2. intervals[i].length == 2
    #3. 0 <= start_i <= end_i <= 105
    #4. intervals is sorted by start_i in ascending order.
    #5. newInterval.length == 2
    #6. 0 <= start <= end <= 105
Refer to: https://leetcode.com/problems/insert-interval/solutions/844549/python-super-short-simple-clean-solution-99-faster/
    Time Complexity: O(n)?
    Space Complexity: O(n)?
Date: 231207.
Created by JSheng <jasonhuang0124@gmail.com>"""

# # For Function Annotations.
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            # # The new interval's range is before the other, so we can add the
            # # new interval and update it to the current one.
            if i[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = i
            # # The new interval is after the range of other interval, so we
            # # can leave the current interval baecause the new one does not
            # # overlap with it.
            elif i[1] < newInterval[0]:
                res.append(i)
            # # The new interval is in the range of the other interval, we have
            # # an overlap, so we must choose the min for start and max for end
            # # of interval.
            else:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])
        res.append(newInterval)
        return res


if __name__ == '__main__':
    qwe = Solution()

    """Should return `[[1,5],[6,9]]`."""
    print(qwe.insert([[1, 3], [6, 9]], [2, 5]))

    """Should return `[[1,2],[3,10],[12,16]]`."""
    print(qwe.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
