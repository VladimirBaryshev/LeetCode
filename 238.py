# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

print('nums=',nums)

res = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
	print(f'i={i}', f'nums[i]={nums[i]}', f'prefix={prefix}', f'res={res}')
	res[i] = prefix
	prefix *= nums[i]
	print(f'i={i}', f'nums[i]={nums[i]}', f'prefix={prefix}', f'res={res}\n')

print('res=', res, '\n')

postfix = 1
for i in range(len(nums)-1, -1, -1):
	print(f'i={i}', f'nums[i]={nums[i]}', f'postfix={postfix}', f'res={res}')
	res[i] *= postfix
	postfix *= nums[i] # !!!
	print(f'i={i}', f'nums[i]={nums[i]}', f'postfix={postfix}', f'res={res}\n')

print('res=', res, '\n')
