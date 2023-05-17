# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

nums = [] # --> 0

nums_0 = [0] # --> 1

nums_1 = [-1, 0] # --> 2

nums_2 = [100,4,200,1,3,2] # --> 4

nums_3 = [0,3,7,2,5,8,4,6,0,1] # --> 9

nums_4 = [1,2,3,4] # --> 4

nums_5 = [1,2,4,5,6] # --> 3


def longestConsecutive(nums):
	
	SetNums = set(nums) #O(N)

	longest = 0

	if len(nums) == 0:
		return longest

	for i in nums: #O(N)

		if (i - 1) not in SetNums:
			lenght = 1

			while (i + lenght) in SetNums: #O(N)
				lenght += 1

			longest = max(longest, lenght)

	return longest


# Time and space complexity = O(N)


print(longestConsecutive(nums))
print(longestConsecutive(nums_0))
print(longestConsecutive(nums_1))
print(longestConsecutive(nums_2))
print(longestConsecutive(nums_3))
print(longestConsecutive(nums_4))








