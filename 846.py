# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/


from typing import List
import heapq


def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    
    if len(hand) % groupSize != 0:
        return False
    # else:
    #   return True

    count = dict()

    for i in hand:
        count[i] = 1+count.get(i, 0)

    minH = list(count.keys())
    heapq.heapify(minH)

    while minH:

        min_value = minH[0]

        for i in range(min_value, min_value+groupSize):

            if i not in count.keys():
                return False
            count[i] -= 1

            if count[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)

    return True





hand_1 = [1,2,3,6,2,3,4,7,8]
groupSize_1 = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

hand_2 = [1,2,3,4,5]
groupSize_2 = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

print(isNStraightHand(hand_1, groupSize_1))
print(isNStraightHand(hand_2, groupSize_2))