# 2405. Optimal Partition of String



class Solution:

    def partitionString(self, s: str) -> int:
        
        result = []
        cur = []
        for i in s:
            if i in cur:
                result.append(cur)
                cur = [i]
            else:
                cur.append(i)
        result.append(cur)
        return len(result)




s_1 = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

s_2 = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
 
print(Solution().partitionString(s_1))
print(Solution().partitionString(s_2))

