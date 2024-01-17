# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:

    intervals.sort(key=lambda x: x[0])
    prevEnd = intervals[0][1]
    count = 0

    for start, end in intervals[1:]:

        if start < prevEnd:
            count += 1
            prevEnd = min(prevEnd, end)
        else:
            prevEnd = end

    return count








intervals_1 = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

intervals_2 = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

intervals_3 = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

print(eraseOverlapIntervals(intervals_1))
print(eraseOverlapIntervals(intervals_2))
print(eraseOverlapIntervals(intervals_3))


