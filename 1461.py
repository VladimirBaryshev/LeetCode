# 1461. Check If a String Contains All Binary Codes of Size K


class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        
        combinations = []
        stack = ['0', '1']

        while stack:

            item = stack.pop()
            if len(item) < k:
                for i in ['0', '1']:
                    stack.append(item[:] + i)
            else:
                combinations.append(item)

        d = dict([(i,0) for i in combinations])
        i = 0
        while i < len(s):
            if s[i:i+k] in d.keys():
                d[s[i:i+k]] += 1
            i += 1  

        if len([v for k,v in d.items() if v == 0]) > 0:
            return False
        else:
            return True







s_1 = "00110110"
k_1 = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". 
# They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

s_2 = "0110"
k_2 = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

s_3 = "0110"
k_3 = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.

print(Solution().hasAllCodes(s_1, k_1))
print(Solution().hasAllCodes(s_2, k_2))
print(Solution().hasAllCodes(s_3, k_3))
 

