# 1436. Destination City


from typing import List
from collections import defaultdict

class Solution:

    def destCity(self, paths: List[List[str]]) -> str:

        d = defaultdict(int)

        for c1, c2 in paths:
            d[c1] += 1
            d[c2]

        return [k for k,v in d.items() if v == 0][0]


paths_1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" 
# city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

paths_2 = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".

paths_3 = [["A","Z"]]
# Output: "Z"

print(Solution().destCity(paths_1))
print(Solution().destCity(paths_2))
print(Solution().destCity(paths_3))
