# 605. Can Place Flowers


from typing import List


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # EDGES:
        if len(flowerbed) > 1 and (flowerbed[0] == 0) and (flowerbed[1] == 0):
            n -= 1
            flowerbed[0] = 1

        if len(flowerbed) > 1 and (flowerbed[-2] == 0) and (flowerbed[-1] == 0):
            n -= 1
            flowerbed[-1] = 1

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
            flowerbed[0] = 1

        # MAIN:
        for i in range(1, len(flowerbed)-1):

            if (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0) and (flowerbed[i] != 1):
                n -= 1
                flowerbed[i] = 1

            if n == 0:
                return True

        if n <= 0:
            return True    
        return False




flowerbed_1 = [1,0,0,0,1]
n_1 = 1
# Output: true

flowerbed_2 = [1,0,0,0,1]
n_2 = 2
# Output: false

flowerbed_3 = [1,0,0,0,0,1]
n_3 = 2
# Output: false

flowerbed_4 = [1,0,1,0,1,0,1]
n_4 = 1
# Output: false

flowerbed_5 = [0,0,1,0,1]
n_5 = 1
# Output: true

flowerbed_6 = [0]
n_6 = 1
# Output: true

flowerbed_7 = [0,0,1,0,0]
n_7 = 1
# Output: true

flowerbed_8 = [0,0,0,0,1]
n_8 = 2
# Output: true

# print(Solution().canPlaceFlowers(flowerbed_1, n_1))
# print(Solution().canPlaceFlowers(flowerbed_2, n_2))
# print(Solution().canPlaceFlowers(flowerbed_3, n_3))
# print(Solution().canPlaceFlowers(flowerbed_4, n_4))
# print(Solution().canPlaceFlowers(flowerbed_5, n_5))
# print(Solution().canPlaceFlowers(flowerbed_6, n_6))
print(Solution().canPlaceFlowers(flowerbed_7, n_7))
print(Solution().canPlaceFlowers(flowerbed_8, n_8))








