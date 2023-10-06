# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq



def last_stone(stones: List[int]) -> int:

    stones = [i*-1 for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        cur_1 = heapq.heappop(stones)
        cur_2 = heapq.heappop(stones)
        
        if cur_1 == cur_2:
            continue
        else: 
            rest_weight = cur_1 - cur_2
            print(cur_1, cur_2, rest_weight)
            heapq.heappush(stones, rest_weight)

    if len(stones) == 1:    
        return abs(heapq.heappop(stones))
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


print(last_stone(stones_1))
print(last_stone(stones_2))
print(last_stone(stones_3))
