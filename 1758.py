# 1758. Minimum Changes To Make Alternating Binary String


class Solution:

    def minOperations(self, s: str) -> int:
        
        etalon_1 = []
        etalon_2 = []

        for i in range(len(s)):

            if i % 2 == 0:
                etalon_1.append("0")
                etalon_2.append("1")
            else:
                etalon_1.append("1")
                etalon_2.append("0")

        etalon_1_count = 0
        etalon_2_count = 0

        for i, e in enumerate(zip(etalon_1, etalon_2)):
            if s[i] != e[0]:
                etalon_1_count += 1
            if s[i] != e[1]:
                etalon_2_count += 1

        return min(etalon_1_count, etalon_2_count)

s_1 = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

s_2 = "10"
# Output: 0
# Explanation: s is already alternating.

s_3 = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".



print(Solution().minOperations(s_1))
print(Solution().minOperations(s_2))
print(Solution().minOperations(s_3))

