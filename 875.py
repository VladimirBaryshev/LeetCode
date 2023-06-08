# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/


import math


piles_1 = [3,6,7,11]
h_1 = 8
# Output: 4

piles_2 = [30,11,23,4,20]
h_2 = 5
# Output: 30

piles_3 = [30,11,23,4,20]
h_3 = 6
# Output: 23


def minEatingSpeed(piles: list[int], h: int) -> int:

    l = 1
    r = max(piles)
    res = max(piles)

    while l <= r:

        k = (l + r) // 2

        totalTime = 0

        for p in piles:

            totalTime += math.ceil(p / k)

        if totalTime <= h:
            res = min(res, k)
            r = k - 1 
        
        else:
            l = k + 1

    return res





print(minEatingSpeed(piles_1, h_1))
print(minEatingSpeed(piles_2, h_2))
print(minEatingSpeed(piles_3, h_3))


