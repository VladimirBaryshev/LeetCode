# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/


from typing import List

def isPalindrome(s: str) -> bool:

    return s == s[::-1]

def partition(s: str) -> List[List[str]]:
    
    result = []

    stack = [[0, []]]
    
    while stack:

        idx, subset = stack.pop()

        if idx == len(s) and subset == []:

            candidate = ["".join(i[1]) for i in stack]
            if sum([isPalindrome(i) for i in candidate]) == len(candidate):
                result.append(candidate)

        if idx < len(s):
            subset.append(s[idx])

            stack.append([idx+1, subset[::]])

            subset.pop()

            stack.append([idx+1, subset[idx::]])

    return result


s_1 = "aab"
# Output: [["a","a","b"],["aa","b"]]

s_2 = "a"
# Output: [["a"]]

s_3 = "aaab"
# output: [["a","a","a","b"],["a","aa","b"],["aa","a","b"],["aaa","b"]]

s_4 = "abcaa"
# output: [["a","b","c","a","a"],["a","b","c","aa"]]

s_5 = "abbab"
# output: [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]

s_6 = "abaca"
# output: [["a","b","a","c","a"],["a","b","aca"],["aba","c","a"]]

s_7 = "aaa"
# output: [["a","a","a"],["a","aa"],["aa","a"],["aaa"]]

print(partition(s_1))
print(partition(s_2))
print(partition(s_3))
print(partition(s_4))
print(partition(s_5))
print(partition(s_6))
print(partition(s_7))





