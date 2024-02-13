# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

def reverse(x: int) -> int:

	if x == 0:
		return 0

    result = ''

    minus = 1

    if x < 0:
        minus = -1

    x = abs(x)
    while x:
        digit = x % 10
        x = x // 10
        result += str(digit)

    
    result = int(result) * minus
    if -2**31 < result < 2**31 -1:
        return result
    return 0


x_1 = 123
# Output: 321

x_2 = -123
# Output: -321

x_3 = 120
# Output: 21

print(reverse(x_1))
print(reverse(x_2))
print(reverse(x_3))