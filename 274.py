# 274. H-Index
# https://leetcode.com/problems/h-index/description/


from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        for i, num in enumerate(citations):
            if len(citations)-i <= num:
                return len(citations)-i

        return 0




citations_1 = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers 
# in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining
 # two with no more than 3 citations each, their h-index is 3.

citations_2 = [1,3,1]
# Output: 1

citations_3 = [11,15]
# Output: 2

citations_4 = [0]
# Output: 0

citations_5 = [100]
# Output: 1


print(Solution().hIndex(citations_1))
print(Solution().hIndex(citations_2))
print(Solution().hIndex(citations_3))
print(Solution().hIndex(citations_4))
print(Solution().hIndex(citations_5))


