# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter


case_1 = ["ab", "eidbaooo"]
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

case_2 = ["ab", "eidboaoo"]
# Output: false


case_3 = ["ab", "eidbobaoo"]
# Output: true


def checkInclusion(s1: str, s2: str) -> bool:

    cntr, w = Counter(s1), len(s1)   

    for i in range(len(s2)):
        
        if s2[i] in cntr:
            # print('minus', i, s2[i])

            # print(cntr)
            cntr[s2[i]] -= 1
            # print(cntr)

        if i >= w and s2[i-w] in cntr:
            # print('plus', i, w, s2[i-w])

            # print(cntr)
            cntr[s2[i-w]] += 1
            # print(cntr)

        if all([cntr[i] == 0 for i in cntr]):
            return True

    return False





print(checkInclusion(*case_1))
print('\n')
print(checkInclusion(*case_2))
print('\n')
print(checkInclusion(*case_3))



