# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/


from typing import List


def countBits(n: int) -> List[int]:

    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset*2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp




n_1 = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

n_2 = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


print(countBits(n_1))
print(countBits(n_2))



