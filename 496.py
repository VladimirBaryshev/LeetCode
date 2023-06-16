# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

nums1_1 = [4,1,2]
nums2_1 = [1,3,4,2]
# Output: [-1,3,-1]


nums1_2 = [2,4]
nums2_2 = [1,2,3,4]
# Output: [3,-1]


nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1, 7 ]
# [7,-1,-1,-1,-1]
# Output: [7,7,7,7,7]

def  next_greater_element(nums1: list[int] , nums2: list[int]) -> list[int]:

    nums1Idx = { n:i for i, n in enumerate(nums1) }
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        cur = nums2[i]

        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = nums1Idx[val]
            res[idx] = cur

        if cur in nums1Idx:
            stack.append(cur)
        
    return res


print(next_greater_element(nums1_1, nums2_1))
print(next_greater_element(nums1_2, nums2_2))
print(next_greater_element(nums1, nums2))








