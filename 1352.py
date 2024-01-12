# 1352. Product of the Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/description/


class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:

        if num > 0:
            self.nums.append(self.nums[-1]*num)
        else:
            self.nums = [1]

    def getProduct(self, k: int) -> int:
        
        last_idx = len(self.nums)-1
        # print(self.nums, last_idx, k)
        if last_idx < k:
            return 0
        else:
            return int(self.nums[last_idx] / self.nums[last_idx-k])



t = ProductOfNumbers()
t.add(3) # [3]
t.add(0) # [3,0]
t.add(2) # [3,0,2]
t.add(5) # [3,0,2,5]
t.add(4) # [3,0,2,5,4]
# print(t.getProduct(2)) # return 20. The product of the last 2 numbers is 5 * 4 = 20
# print(t.getProduct(3)) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# print(t.getProduct(4)) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
t.add(8) # [3,0,2,5,4,8]
print(t.getProduct(2)) #  return 32. The product of the last 2 numbers is 4 * 8 = 32 

