# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/


from typing import List


def change(amount: int, coins: List[int]) -> int:
    

    dp = [0]*(amount+1)
    dp[0] = 1

    for i in range(len(coins)-1,-1,-1):
        next_dp = [0]*(amount+1)
        next_dp[0] = 1

        for a in range(1, amount+1):
            next_dp[a] = dp[a] 
            if a - coins[i] >= 0:
                next_dp[a] += next_dp[a - coins[i]]

        dp = next_dp        

    return dp[amount]

amount_1 = 5
coins_1 = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

amount_2 = 3
coins_2 = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

amount_3 = 10
coins_3 = [10]
# Output: 1

amount_4 = 0
coins_4 = [7]
# Output: 1


print(change(amount_1, coins_1))
print(change(amount_2, coins_2))
print(change(amount_3, coins_3))
print(change(amount_4, coins_4))

