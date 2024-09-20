# 1624. Largest Substring Between Two Equal Characters


from typing import defaultdict


class Solution:

    def maxLengthBetweenEqualCharacters(self, string: str) -> int:

        d = defaultdict(list)

        for i, s in enumerate(string):
            d[s].append(i)

        result = -1

        for k,v in d.items():
            if len(v) > 1:
                min_i, max_i = v[0], v[-1]
                substr = string[min_i: max_i+1]
                result = max(result, len(substr)-2)

        return result




s_1 = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.

s_2 = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".

s_3 = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

print(Solution().maxLengthBetweenEqualCharacters(s_1))
print(Solution().maxLengthBetweenEqualCharacters(s_2))
print(Solution().maxLengthBetweenEqualCharacters(s_3))


