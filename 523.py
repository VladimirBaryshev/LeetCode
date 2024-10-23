# 523. Continuous Subarray Sum


from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # if not nums:
        #     return False

        hist = set()

        last = 0
        for num in nums:

            item = (last + num)%k
            if item in hist:
                return True

            hist.add(last)
            last = item

        return False



nums_1 = [23,2,4,6,7]
k_1 = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

nums_2 = [23,2,6,4,7]
k_2 = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

nums_3 = [23,2,6,4,7]
k_3 = 13
# Output: false

nums_4 = [23,2,4,6,6]
k_4 = 7
# Output: true

# print(Solution().checkSubarraySum(nums_1, k_1))
# print(Solution().checkSubarraySum(nums_2, k_2))
# print(Solution().checkSubarraySum(nums_3, k_3))
print(Solution().checkSubarraySum(nums_4, k_4))





