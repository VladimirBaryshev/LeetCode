# Дан массив чисел, содержащий минимум два элемента. 
# Нужно найти максимальное произведение двух элементов в этом массиве.

# Пример:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 16
# Explanation: 4 * 4 = 16


from typing import List

def find_pair(nums: List[int]) -> int:
    
    min_val1, min_val2 = 0, 0
    max_val1, max_val2 = 0, 0

    for num in nums:

        if num < 0:

            if num < min_val1:
                min_val1, min_val2 = num, min_val1

            elif num < min_val2:
                min_val2 = num

        elif num > 0:

            if num > max_val1:
                max_val1, max_val2 = num, max_val1

            elif num > max_val2:
                max_val2 = num

    return max((min_val1 * min_val2), (max_val1*max_val2))
        


nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #16
nums_2 = [-2, 1, -5, 4, -1, 2, 1, -5, 4] #25
nums_3 = [0,0] #0
nums_4 = [-1,-1] #1
nums_5 = [-1,0] #0


print(find_pair(nums_1))
print(find_pair(nums_2))
print(find_pair(nums_3))
print(find_pair(nums_4))
print(find_pair(nums_5))




