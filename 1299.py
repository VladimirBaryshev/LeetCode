# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

def replace_among_the_right(arr):

    r = []

    max_prev = -1
    
    for i in range(len(arr)-1,-1,-1):

        curr = arr[i]
        arr[i] =  max_prev

        max_prev = max(curr, max_prev)

    return arr


arr_1 = [17,18,5,4,6,1] #Output: [18,6,6,6,1,-1]
arr_2 = [400] #Output: [-1]



print(replace_among_the_right(arr_1))
print(replace_among_the_right(arr_2))

