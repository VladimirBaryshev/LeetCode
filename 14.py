# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/


from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = tuple(zip(*strs))

        substr = ""

        for i in strs:

            if len(set(i)) == 1:
                substr += i[0]
            else:
                break

        return substr



strs_1 = ["flower","flow","flight"]
# Output: "fl"

strs_2 = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

strs_3 = ["cir","car"] 
# Output:"c"

print(Solution().longestCommonPrefix(strs_1))
print(Solution().longestCommonPrefix(strs_2))
print(Solution().longestCommonPrefix(strs_3))
