# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

s_1 = "ABAB"
k_1 = 2
# Output: 4

s_2 = "AABABBA"
k_2 = 1
# Output: 4

def charRepl(s: str, k: int) -> int: # "ABA B ", 2

    count = {} #{'A': 2, 'B': 2}
    res = 0 # 4

    l = 0 # 0
    maxf = 0 # 2

    for r in range(len(s)): # 3
        count[s[r]] = 1 + count.get(s[r], 0) # 1 + 1
        maxf = max(maxf, count[s[r]]) # (2,2)

        if (r - l + 1) - maxf > k: # (3 - 0 + 1) - 2 > 2 --> False
            count[s[l]] -= 1 # ...
            l += 1 # ...

        res = max(res, r - l + 1) # (3, 3 - 0 + 1) --> 4

    return res

print(charRepl(s_1, k_1))
print(charRepl(s_2, k_2))



