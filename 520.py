# 520. Detect Capital
# https://leetcode.com/problems/detect-capital/description/

class Solution:

    def detectCapitalUse(self, word: str) -> bool:

        if word.islower():
            return True

        if word.isupper():
            return True

        if word[0].isupper() and word[1:].islower(): # istitle()
            return True



