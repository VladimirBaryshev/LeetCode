# 848. Shifting Letters
# https://leetcode.com/problems/shifting-letters/description/


from typing import List


def shiftingLetters(s: str, shifts: List[int]) -> str:
    
    str_to_int = {chr(96 + i) : i  for i in range(1, 27)}
    int_to_str = {i : chr(96+i) for i in range(1, 27)}

    prefix_sum = 0
    new_shifts = []

    for i in range(len(shifts)-1, -1, -1):
        new_shifts.append(prefix_sum+shifts[i])
        prefix_sum += shifts[i]

    new_shifts = reversed(new_shifts)

    # print(s, list(new_shifts))

    result = ""

    for l, int_shift in zip(s, new_shifts):

        l_index = str_to_int[l]
        new_index = (l_index + int_shift) % 26

        # print(l, l_index, int_shift, l_index+int_shift, new_index)

        if new_index > 0: 
            result += int_to_str[new_index]
        else:
            result += 'z'

    return result


s_1 = "abc"
shifts_1 = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

s_2 = "aaa"
shifts_2 = [1,2,3]
# Output: "gfd"

s_3 = "z"
shifts_3 = [52]
# Output: "z"

s_4 = "qoqpvw"
shifts_4 = [95,7,67,21,33,23]
# Output: "cjeozt"

print(shiftingLetters(s_1, shifts_1))
print(shiftingLetters(s_2, shifts_2))
print(shiftingLetters(s_3, shifts_3))
print(shiftingLetters(s_4, shifts_4))

