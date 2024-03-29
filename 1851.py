# 1851. Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/

import heapq
from typing import List

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    
    intervals.sort()
    minHeap = []
    res = {}
    i = 0
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(minHeap, (r - l + 1, r))
            i += 1

        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)
        res[q] = minHeap[0][0] if minHeap else -1
    return [res[q] for q in queries]
        


intervals_1 = [[1,4],[2,4],[3,6],[4,4]]
queries_1 = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

intervals_2 = [[2,3],[2,5],[1,8],[20,25]]
queries_2 = [2,19,5,22]
# Output: [2,-1,4,6]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
# - Query = 19: None of the intervals contain 19. The answer is -1.
# - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
# - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

intervals_3 = [[9,9],[6,7],[5,6],[2,5],[3,3]]
queries_3 = [6,1,1,1,9]

print(minInterval(intervals_1, queries_1))
print(minInterval(intervals_2, queries_2))
print(minInterval(intervals_3, queries_3))




