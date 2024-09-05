# 303. Range Sum Query - Immutable


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))

# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3