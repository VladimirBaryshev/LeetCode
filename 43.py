# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/description/

def multiply(num1: str, num2: str) -> str:
    
    if "0" == num1 or "0" == num2:
        return "0"

    res = [0] * (len(num1)+len(num2))

    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(len(num1)):
        for j in range(len(num2)):
            digit = int(num1[i]) * int(num2[j])
            res[i+j] += digit
            res[i+j+1] += res[i+j]//10
            res[i+j] = res[i+j]%10

    while res[-1] == 0:
        res.pop()

    return "".join(map(str, res[::-1]))




num1_1 = "2"
num2_1 = "3"
# Output: "6"

num1_2 = "123"
num2_2 = "456"
# Output: "56088"

print(multiply(num1_1, num2_1))
print(multiply(num1_2, num2_2))
