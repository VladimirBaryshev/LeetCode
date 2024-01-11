# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/

from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                
                result.append(newInterval)
                return result+intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result        
        


intervals_1 = [[1,3],[6,9]]
newInterval_1 = [2,5]
# Output: [[1,5],[6,9]]

intervals_2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval_2 = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

print(Solution().insert(intervals_1, newInterval_1))
print(Solution().insert(intervals_2, newInterval_2))




