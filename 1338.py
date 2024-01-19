# 1338. Reduce Array Size to The Half
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/


from typing import List
from collections import defaultdict

def minSetSize(arr: List[int]) -> int:
    '''
    while num_removed < length // 2:
        elm, freq = value_counts.pop(0)
        num_removed += freq
        minset += 1
    '''
    # value_counts = {7: 6}
    # num_removed = 0, len(arr) = 6
    # get counts = 6 , num_removed -> mindset+= 1
    
    minSet = 0
    num_removed = 0
    value_counts = defaultdict(int)
    for i in arr:
        value_counts[i] += 1

    value_counts = sorted(value_counts.items(), key=lambda x: x[1])

    for k,v in value_counts[::-1]:
        if num_removed < len(arr) // 2:
            num_removed += v
            minSet += 1
        else:
            return minSet
    return minSet


arr_1 = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

arr_2 = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.

print(minSetSize(arr_1))
print(minSetSize(arr_2))

