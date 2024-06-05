# 77. Combinations
# https://leetcode.com/problems/combinations/description/


from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        r = []
        queue = list([[i], 1] for i in range(1, n+1))

        while queue:
            elem, lenght = queue.pop(0)
            if lenght < k:
                for i in range(elem[-1]+1, n+1):
                    queue.append([elem.copy()+[i], lenght+1])
            else:
                r.append(elem)
        return r




n_1 = 4
k_1 = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] 
# are considered to be the same combination.

n_2 = 1
k_2 = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

print(Solution().combine(n_1, k_1))
print(Solution().combine(n_2, k_2))