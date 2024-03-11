# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/


from typing import List


def maxProfit(prices: List[int]) -> int:
    
    dp = dict()

    def dfs(i, buying_status):
        
        if i >= len(prices):
            return 0
        if (i, buying_status) in dp:
            return dp[(i, buying_status)]

        cooldown = dfs(i+1, buying_status)

        if buying_status:
            buy = dfs(i+1, not buying_status) - prices[i]
            dp[(i, buying_status)] = max(cooldown, buy)
        else:
            sell = dfs(i+2, not buying_status) + prices[i]
            dp[(i, buying_status)] = max(cooldown, sell)
        return dp[(i, buying_status)]

    return dfs(0, True)



prices_1 = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

prices_2 = [1]
# Output: 0        

print(maxProfit(prices_1))
print(maxProfit(prices_2))




