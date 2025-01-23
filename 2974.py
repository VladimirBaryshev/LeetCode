# 2974. Minimum Number Game

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        result = []
        nums = sorted(nums)

        while nums:
            A = nums.pop(0)
            B = nums.pop(0)
            result.append(B)
            result.append(A)

        return result

        

nums_1 = [5,4,2,3]
# Output: [3,2,5,4]
# Explanation: In round one, first Alice removes 2 and then Bob removes 3. 
# Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
# At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. 
# Then both append in arr which becomes [3,2,5,4].

nums_2 = [2,5]
# Output: [5,2]
# Explanation: In round one, first Alice removes 2 and then Bob removes 5. 
# Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].
 
print(Solution().numberGame(nums_1))
print(Solution().numberGame(nums_2))