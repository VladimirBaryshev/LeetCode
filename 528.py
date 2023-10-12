# 528. Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/description/

from typing import List
import random
import bisect

class Solution:
    
    def __init__(self, w: List[int]):
        sum = 0
        self.a = []
        for i in w:
            sum += i
            self.a.append(sum)
        self.total = sum 
        

    def pickIndex(self) -> int:
        ran = random.randint(1, self.total)
        return bisect.bisect_left(self.a, ran)
      



t_1 = Solution([1])
print(t_1.pickIndex())
# Output [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. 
# The only option is to return 0 since there is only one element in w.

t_2 = Solution([1,3])
print(t_2.pickIndex())
print(t_2.pickIndex())
print(t_2.pickIndex())
print(t_2.pickIndex())
print(t_2.pickIndex())
# Output [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
