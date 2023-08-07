# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

'''
Edge and constraints:
1 < len(nums) < 10**5
nums is ints from -2**31 to 2**31
some nums without zeros
some nums consists only zeros elems
don't need to sort nonzeros elems
'''

def moveZeros(nums):

    '''
        get 2 pointers
        use 1st one to iterate array 
    '''

    zero_counter = 0

    for i in nums:

        if i == 0:
            zero_counter += 1


    prev_nonzero_idx = 0
    for curr_idx, curr_value in enumerate(nums):

        if curr_value != 0:
            nums[prev_nonzero_idx] = curr_value
            prev_nonzero_idx += 1


    padding_start_idx = len(nums) - zero_counter
    for curr_idx in range(prev_nonzero_idx, len(nums)):
            nums[curr_idx] = 0
    
    return nums



nums_1 = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums_2 = [0]
# Output: [0]



print(moveZeros(nums_1))
print(moveZeros(nums_2))





