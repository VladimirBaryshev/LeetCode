# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/description/

def multiply(num1: str, num2: str) -> str:
    
    return str(int(num1) * int(num2))


num1_1 = "2"
num2_1 = "3"
# Output: "6"

num1_2 = "123"
num2_2 = "456"
# Output: "56088"

print(multiply(num1_1, num2_1))
print(multiply(num1_2, num2_2))
