# 1963. Minimum Number of Swaps to Make the String Balanced


class Solution:

    def minSwaps(self, s: str) -> int:
        
        count = 0

        for i in s:
            if i == "[":
                count += 1
            else:
                if count > 0:
                    count -=1

        return (count + 1) // 2


s_1 = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".

s_2 = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".

s_3 = "[]"
# Output: 0
# Explanation: The string is already balanced.

print(Solution().minSwaps(s_1))
print(Solution().minSwaps(s_2))
print(Solution().minSwaps(s_3))

