# 66. Plus One
# https://leetcode.com/problems/plus-one/description/


from typing import List


def plusOne(digits: List[int]) -> List[int]:
    
    digits = "".join((str(i) for i in digits))
    digits = int(digits) 
    digits += 1
    digits = str(digits)
    digits = [int(i) for i in digits]

    return digits


digits_1 = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

digits_2 = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

digits_3 = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


print(plusOne(digits_1))
print(plusOne(digits_2))
print(plusOne(digits_3))