# 2442. Count Number of Distinct Integers After Reverse Operations
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/


from typing import List

# Edges and constraints:
# nums[i] > 0
# 10**24 > len(nums) > 0

# Ideas:

# # HINT: Convert each num to string

# Create set of distinct vals
# iterate over nums
#   If str(nums[i]) in distinct_set += count
#   if reversed(str(nums[i])) in distinct_set += count
#       Don’t forget vals that ends with 0. We need to cut after reverse


def countDistinctIntegers(nums: List[int]) -> int:
    
    distinct_vals = set()

    for i in nums:

        distinct_vals.add(i)
        i = str(i)
        i = int("".join(reversed(i)))
        distinct_vals.add(i)

    return len(distinct_vals)




nums_1 = [1,13,10,12,31]
# Output: 6
# Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
# The reversed integers that were added to the end of the array are underlined. 
# Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
# The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).

nums_2 = [2,2,2]
# Output: 1
# Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2].
# The number of distinct integers in this array is 1 (The number 2).


print(countDistinctIntegers(nums_1))
print(countDistinctIntegers(nums_2))


