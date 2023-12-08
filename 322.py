# 322. Coin Change
# https://leetcode.com/problems/coin-change/


from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        print(dp)

        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    print(a, coin, dp)
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1






coins_1 = [1,2,5]
amount_1 = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

coins_2 = [2]
amount_2 = 3
# Output: -1

coins_3 = [1]
amount_3 = 0
# Output: 0

print(Solution().coinChange(coins_1, amount_1))
# print(Solution().coinChange(coins_2, amount_2))
# print(Solution().coinChange(coins_3, amount_3))



