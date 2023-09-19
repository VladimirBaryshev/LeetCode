# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:

    while len(stones) > 1:

        heapq._heapify_max(stones)
        y = heapq.heappop(stones)
        heapq._heapify_max(stones)
        x = heapq.heappop(stones)

        if x == y:
            continue
        else:
            y = y - x
            stones.append(y)

    if len(stones) == 1:
        heapq._heapify_max(stones)
        return heapq.heappop(stones)
    else:
        return 0


stones_1 = [2,7,4,1,8,1] # Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

stones_2 = [1] # Output: 1

stones_3 = [2,2] # Output: 0

print(lastStoneWeight(stones_1))
print(lastStoneWeight(stones_2))
print(lastStoneWeight(stones_3))