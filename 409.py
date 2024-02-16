# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/description/

from collections import defaultdict


def longestPalindrome(s: str) -> int:

    counter = defaultdict(int)
    
    for i in s:
        counter[i] += 1

    res = 0

    is_odd_in_counter = False

    for k,v in counter.items():

        if v % 2 == 0:
            res += v
            # counter[k] -= v
        else:
            res += (v-1)
            # counter[k] = 1
            is_odd_in_counter = True

    if is_odd_in_counter:
        res += 1

    return res




s_1 = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

s_2 = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

s_3 = "adam"
# Output: 3

print(longestPalindrome(s_1))
print(longestPalindrome(s_2))
print(longestPalindrome(s_3))






