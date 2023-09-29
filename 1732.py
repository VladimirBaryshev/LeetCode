# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/


from typing import List


def findHighestPoint(gains: List[int]) -> int:
    
    altitudes = [0]
    max_alt = 0

    for gain in gains:
            new_alt = altitudes[-1] + gain
            altitudes.append(new_alt)

            if new_alt > max_alt:
                max_alt = new_alt

    return max_alt


gain_1 = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

gain_2 = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

print(findHighestPoint(gain_1))
print(findHighestPoint(gain_2))