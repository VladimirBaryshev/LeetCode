# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/description/


from typing import List


def partitionLabels(s: str) -> List[int]:
    
    last_index = dict()

    for i, c in enumerate(s):
        last_index[c] = i

    result = []
    size, end = 0, 0

    for i, c in enumerate(s):
        
        size += 1
        end = max(end, last_index[c])
        
        if i == end:
            result.append(size)
            size = 0

    return result







s_1 = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

s_2 = "eccbbbbdec"
# Output: [10]


print(partitionLabels(s_1))
print(partitionLabels(s_2))

