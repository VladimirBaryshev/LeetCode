# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

height_1 = [1,8,6,2,5,4,8,3,7] # 49
height_2 = [1,1] # 1


def maxArea(height: list[int]) -> int:
    
    l = 0
    r = len(height) - 1
    h = max(height)

    res = 0

    while l < r:
        temp_res = (min(height[l], height[r]) * (r-l))
        res = max(res, temp_res)

        if height[l] < height[r]:
            l += 1
        elif height[l] >= height[r]:
            r -= 1

    return res

print(maxArea(height_1))
print(maxArea(height_2))