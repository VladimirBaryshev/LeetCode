# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/description/


from typing import List


class Solution:

    def list_to_str(self, rang: List[int]):
        
        if len(rang) == 1:
            return str(rang[0])
        else:
            return str(rang[0]) + "->" + str(rang[-1])



    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []

        if len(nums) == 0:
            return res

        cur = nums.pop(0)
        rang = [cur]

        while nums:
            cur = nums.pop(0)
            if rang[-1]+1 == cur:
                rang.append(cur)
            else:
                res.append(self.list_to_str(rang))
                rang = [cur]

        res.append(self.list_to_str(rang))      
        return res



nums_1 = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

nums_2 = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"      

print(Solution().summaryRanges(nums_1))
print(Solution().summaryRanges(nums_2))




