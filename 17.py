# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


from typing import List


def letterCombinations(digits: str) -> List[str]:

    if len(digits) == 0:
        return []

    keyboard = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                }

    result = []
    stack = [[0, []]]

    while stack:

        idx, combination = stack.pop()
        if len(combination) == len(digits):
            result.append("".join(combination))

        if idx < len(digits):
            for char in keyboard[digits[idx]]:
                # print(stack)
                combination.append(char)
                stack.append([idx+1, combination[::]])
                combination.pop()


    return result



digits_1 = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits_2 = ""
# Output: []

digits_3 = "2"
# Output: ["a","b","c"]


print(letterCombinations(digits_1))
print(letterCombinations(digits_2))
print(letterCombinations(digits_3))


