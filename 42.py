# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

def count_cap(height: List[int]) -> int:
    
    total = 0
    max_lefts = []
    max_rights = []
        
    max_l = 0
    for i,l_val in enumerate(height):
        max_l = max(max_l, l_val)
        max_lefts.append(max_l)

    max_r = height[-1]
    for i,r_val in enumerate(reversed(height)):
        max_r = max(max_r, r_val)
        max_rights.append(max_r)
    max_rights.reverse()


    print(max_lefts)
    print(max_rights)

    for i in range(len(height)):
        y = min(max_lefts[i], max_rights[i])
        if y > height[i]:
            cur_val = y - height[i]
            total += cur_val

    return total



height_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

height_2 = [4,2,0,3,2,5]
# Output: 9

print(count_cap(height_1))
print(count_cap(height_2))


