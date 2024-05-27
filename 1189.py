# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = {
            "b" : 0,
            "a" : 0,
            "l" : 0,
            "o" : 0,
            "n" : 0
            }

        for char in text:
            if char in d.keys():
                d[char] += 1

        counter = 0     
        while d["b"] >= 1 and d["a"] >= 1 and d["l"] >= 2 and d["o"] >= 2 and d["n"] >= 1:
            counter += 1

            d["b"] -= 1
            d["a"] -= 1
            d["l"] -= 2
            d["o"] -= 2
            d["n"] -= 1
        
        return counter
