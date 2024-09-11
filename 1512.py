# 1512. Number of Good Pairs


from typing import List


class Solution:

    def numIdenticalPairs_2(self, nums: List[int]) -> int:
        
        d = dict()
        count = 0

        for i in nums:
            if i in d.keys():
                count += d[i]
                d[i] += 1
            else:
                d[i] = 1

        return count


    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = 0 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i < j) and (nums[i] == nums[j]):
                    count += 1

        return count



nums_1 = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

nums_2= [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

nums_3 = [1,2,3]
# Output: 0     

# print(Solution().numIdenticalPairs(nums_1))
# print(Solution().numIdenticalPairs(nums_2))
# print(Solution().numIdenticalPairs(nums_3))
print(Solution().numIdenticalPairs_2(nums_1))
print(Solution().numIdenticalPairs_2(nums_2))
print(Solution().numIdenticalPairs_2(nums_3))

