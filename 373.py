# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


from typing import List
import heapq


class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    
        result = []
        heap = [[sum((nums1[0], nums2[0])), nums1[0], nums2[0], 0, 0]]
        visited = set((0,0))

        while heap and len(result) < k:
            _, num1, num2, i, j = heapq.heappop(heap)
            result.append([num1, num2])

            if i < len(nums1)-1 and (i+1, j) not in visited:
                heapq.heappush(heap, [sum((nums1[i+1], nums2[j])), nums1[i+1], nums2[j], i+1, j])
                visited.add((i+1, j))

            if j < len(nums2)-1 and (i, j+1) not in visited:
                heapq.heappush(heap, [sum((nums1[i], nums2[j+1])), nums1[i], nums2[j+1], i, j+1])
                visited.add((i, j+1))

        return result





nums1_1 = [1,7,11]
nums2_1 = [2,4,6]
k_1 = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: 
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

nums1_2 = [1,1,2]
nums2_2 = [1,2,3]
k_2 = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: 
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

print(Solution().kSmallestPairs(nums1_1, nums2_1, k_1))
print(Solution().kSmallestPairs(nums1_2, nums2_2, k_2))
