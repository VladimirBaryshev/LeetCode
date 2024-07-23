# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = (10**4) + 1 # float("inf")
        res = 0

        for i, cur_val in enumerate(prices):
            
            min_val = min(min_val, cur_val)

            if cur_val > min_val:
                res += (cur_val - min_val)
                min_val = cur_val

        return res








prices_1 = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

prices_2 = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

prices_3 = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

print(Solution().maxProfit(prices_1))
print(Solution().maxProfit(prices_2))
print(Solution().maxProfit(prices_3))





