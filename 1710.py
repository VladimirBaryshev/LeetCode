# 1710. Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/description/


from typing import List

class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        remains = truckSize
        result = 0

        # [[1,3], [2,2], [3,1], [1,4]]
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        # [[3, 1], [2, 2], [1, 3], [1, 4]]

        for num_boxes, number_of_unit in boxTypes:
            num_boxes_used = min(num_boxes, remains)
            remains -= num_boxes_used
            result += num_boxes_used * number_of_unit

            if remains == 0:
                return result

                
        return result
                