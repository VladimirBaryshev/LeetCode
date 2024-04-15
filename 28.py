# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/



class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        l = 0
        r = len(needle)
        
        res = -1

        while r <= len(haystack):

            if haystack[l:r] == needle:

                if res > -1:
                    break
                res = l    

            l += 1
            r += 1

        return res



haystack_1 = "sadbutsad"
needle_1 = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

haystack_2 = "leetcode"
needle_2 = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

print(Solution().strStr(haystack_1, needle_1))
print(Solution().strStr(haystack_2, needle_2))


