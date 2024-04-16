# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/


import collections


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r = collections.defaultdict(int)
        m = collections.defaultdict(int)

        for s in ransomNote:
            r[s] += 1

        for s in magazine:
            m[s] += 1

        for s in r.keys():
            m[s] -= r[s]

        if min(m.values()) < 0:
            return False
        else:
            return True




ransomNote_1 = "a"
magazine_1 = "b"
# Output: false

ransomNote_2 = "aa"
magazine_2 = "ab"
# Output: false

ransomNote_3 = "aa"
magazine_3 = "aab"
# Output: true


print(Solution().canConstruct(ransomNote_1, magazine_1))
print(Solution().canConstruct(ransomNote_2, magazine_2))
print(Solution().canConstruct(ransomNote_3, magazine_3))

