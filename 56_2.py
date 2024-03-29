# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/


from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for i in range(1, len(intervals)):

        if intervals[i][0] <= result[-1][1]:
            result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]
        else:
            result.append(intervals[i])

    return print(result)







intervals_1 = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

intervals_2 = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

intervals_3 = [[1,2]]
# [[1,2]]

intervals_4 = [[1,4],[0,0]]
# [[0,0],[1,4]]

merge(intervals_1)
merge(intervals_2)
merge(intervals_3)
merge(intervals_4)

