# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description



class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
    	
    	return len(set(zip(s,t))) == len(set(s)) == len(set(t))




s_1 = "egg"
t_1 = "add"
# Output: true

s_2 = "foo"
t_2 = "bar"
# Output: false

s_3 = "paper"
t_3 = "title"
# Output: true

print(Solution().isIsomorphic(s_1, t_1))
print(Solution().isIsomorphic(s_2, t_2))
print(Solution().isIsomorphic(s_3, t_3))

