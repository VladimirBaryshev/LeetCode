# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/


def reverseBits(n: int) -> int:
	
	res = 0

	for i in range(32):
		bit = (n >> i)&1
		res = res | (bit << (31 - i))
		# print(bin(n >> i), bit, res)

	return res


n_1 = 0b00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

n_2 = 0b11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
# so return 3221225471 which its binary representation is 10111111111111111111111111111111.


print(reverseBits(n_1))
print(reverseBits(n_2))

