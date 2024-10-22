# 179. Largest Number


from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        
        if sum(nums) == 0:
            return "0"
            
        rank = [i/(10**len(str(i))-1) for i in nums]
        nums = list(zip(rank, nums))
        nums.sort(reverse=True)
        
        return "".join([str(i[1]) for i in nums])


nums_1 = [10,2]
# Output: "210"

nums_2 = [3,30,34,5,9]
# Output: "9534330"

nums_3 = [10,2,9,39,17]
# "93921710"

nums_4 = [0,0]
# "0"

print(Solution().largestNumber(nums_1))
print(Solution().largestNumber(nums_2))
print(Solution().largestNumber(nums_3))
print(Solution().largestNumber(nums_4))
