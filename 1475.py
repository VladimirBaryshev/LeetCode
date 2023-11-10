# 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:

        result = [0 for i in prices]
        stack = [0] # to store indexes

        for i,cur_price in enumerate(prices):
            
            while stack and cur_price <= prices[stack[-1]]:
                prev_i = stack.pop() # example [7,8] , curr_num = 4
                result[prev_i] = prices[prev_i] - cur_price
            stack.append(i)

        while stack:
            prev_i = stack.pop()
            result[prev_i] = prices[prev_i] 
        
        return result



prices_1 = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

prices_2 = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.

prices_3 = [10,1,1,6]
# Output: [9,0,1,6]

print(Solution().finalPrices(prices_1))
print(Solution().finalPrices(prices_2))
print(Solution().finalPrices(prices_3))
