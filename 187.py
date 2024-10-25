# 187. Repeated DNA Sequences
from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        result = defaultdict(int)
        i = 0
        while i < len(s):
            if len(s[i:i+10]) == 10:
                result[s[i:i+10]] += 1
            i += 1

        return [k for k,v in result.items() if v > 1]



s_1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

s_2 = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

s_3 = "A"
# Output: ["A"]

print(Solution().findRepeatedDnaSequences(s_1))
print(Solution().findRepeatedDnaSequences(s_2))
# print(Solution().findRepeatedDnaSequences(s_3))