# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/description/

def helper(x, n):
	
	if x == 0:
		return 0
	if n == 0:
		return 1
	
	res = helper(x*x, n//2)

	if n % 2:
		return x * res
	else:
		return res

def myPow(x: float, n: int) -> float:

	res = helper(x, abs(n))

	if n >= 0:
		return res
	else:
		return 1/res

	






x_1 = 2.00000
n_1 = 10
# Output: 1024.00000

x_2 = 2.10000
n_2 = 3
# Output: 9.26100

x_3 = 2.00000
n_3 = -2
# Output: 0.25000
# Explanation: 2**-2 = 1/2**2 = 1/4 = 0.25

print(myPow(x_1, n_1))
print(myPow(x_2, n_2))
print(myPow(x_3, n_3))