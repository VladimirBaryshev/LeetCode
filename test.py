from typing import List


def letter_combinations(digits: List[str]) -> List[str]:

    if len(digits) == 0:
        return []
    
    num_pad = [
                "",      # 0
                "",      # 1
                "abc",   # 2
                "def",   # 3
                "ghi",   # 4
                "jkl",   # 5
                "mno",   # 6
                "pqrs",  # 7
                "tuv",   # 8
                "wxyz"   # 9
            ]


    stack = [i for i in num_pad[int(digits[0])]] # [a, b, c]

    while stack:
        cur_comb = stack.pop()
        for l in digits[1:]:
            stack.append(cur_comb+l)

        print(stack)

digits = "23"

letter_combinations(digits)        
