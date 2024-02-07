# 1899. Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/


from typing import List


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    
    good_indx = set()

    for t in triplets:

        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        for i,v in enumerate(t):

            if v == target[i]:
                good_indx.add(i)

    return len(good_indx) == 3
       


triplets_1 = [[2,5,3],[1,8,4],[1,7,5]]
target_1 = [2,7,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
# The target triplet [2,7,5] is now an element of triplets.

triplets_2 = [[3,4,5],[4,5,6]]
target_2 = [3,2,5]
# Output: false
# Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

triplets_3 = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target_3 = [5,5,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. 
# Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. 
# triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
# 
# - Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. 
# Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. 
# triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
# The target triplet [5,5,5] is now an element of triplets.




print(mergeTriplets(triplets_1, target_1))
print(mergeTriplets(triplets_2, target_2))
print(mergeTriplets(triplets_3, target_3))

