# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

from typing import List

def maximum_amount_of_water(height: List[int]) -> int:

    max_water_area = 0
    l, r = 0, len(height)-1

    while l < r:
        left_h = height[l]
        right_h = height[r]
        min_scale = min(left_h, right_h)
        curr_water_area = min_scale * (r-l)
        max_water_area = max(max_water_area, curr_water_area)
    
        #greedy solution on moving pointers
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return max_water_area


height_1 = [1,8,6,2,5,4,8,3,7] # 49
height_2 = [1,1] # 1

print(maximum_amount_of_water(height_1))
print(maximum_amount_of_water(height_2))