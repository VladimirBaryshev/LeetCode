# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/


from typing import List


def hammingWeight(n: int) -> int:

    res = 0

    while n:
        # print(bin(n))
        res += n % 2
        n = n >> 1

    return res



n_1 = 0b00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

n_2 = 0b00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

n_3 = 0b11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

print(hammingWeight(n_1))
print(hammingWeight(n_2))
print(hammingWeight(n_3))

