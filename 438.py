# 438. Find All Anagrams in a String

from typing import List
from collections import Counter

class Solution:

    def countSubstring(self, substr: str) -> str:
        
        # we don't use it because Leetcode retuned Time Limit exception
        # but the logic is the same
        # Slower then collections.Counter

        counted = dict()
        for i in substr:
            counted[i] = counted.get(i,0)
            counted[i] += 1
        return counted

    def findAnagrams(self, s: str, p: str) -> List[int]:

        L = len(p)
        # counted = self.countSubstring(p) # Using selfwritten Counter wehave got Time Limit exception
        counted = Counter(p) # Let's use the built-in version of this function.

        result = []
        for i,v in enumerate(s):
            # if self.countSubstring(s[i:i+L]) == counted:
            if Counter(s[i:i+L]) == counted:
                result.append(i)
        return result



s_1 = "cbaebabacd"
p_1 = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

s_2 = "abab"
p_2 = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram

print(Solution().findAnagrams(s_1, p_1))
print(Solution().findAnagrams(s_2, p_2))