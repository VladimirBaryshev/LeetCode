s_1 = "abcabcbb" # Output: 3
# Explanation: The answer is "abc", with the length of 3.

s_2 = "bbbbb" # Output: 1
# Explanation: The answer is "b", with the length of 1.

s_3 = "pwwkew" # Output: 3
# Explanation: The answer is "wke", with the length of 3.


"abc a bcbb"

def lengthOfLongestSubstring(s: str) -> int:

    charSet = set() # {b, с, a}
    l = 0 # 1
    res = 0 # 3

    for i in range(len(s)): # 3 of 7
        while s[i] in charSet: # a
            charSet.remove(s[l]) # a
            l += 1
        charSet.add(s[i]) #a
        res = max(res, i - l + 1) # 3, (3 - 1 + 1) # 3

    return res




print(lengthOfLongestSubstring(s_1))
print(lengthOfLongestSubstring(s_2))
print(lengthOfLongestSubstring(s_3))



