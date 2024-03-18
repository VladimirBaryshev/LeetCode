# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/


from typing import List


def change(amount: int, coins: List[int]) -> int:
    
    if amount == 0:
        return 1

    count = set()
    t = {i:0 for i in coins}
    stack = []

    for c in coins:
        d = {i:0 for i in coins}
        d[c] += 1
        stack.append([d, c])

    while stack:
        temp_d, temp_sum = stack.pop()
        for c in coins:
            temp_d_copy = temp_d.copy()
            if temp_sum == amount:
                count.add(tuple(temp_d_copy.values()))
            if c + temp_sum < amount:
                temp_d_copy[c] += 1
                stack.append([temp_d_copy, temp_sum+c])
            if c + temp_sum == amount:
                temp_d_copy[c] += 1
                count.add(tuple(temp_d_copy.values()))

    return len(count)



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


# print(change(amount_1, coins_1))
# print(change(amount_2, coins_2))
# print(change(amount_3, coins_3))
print(change(amount_4, coins_4))

