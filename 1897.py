# 1897. Redistribute Characters to Make All Strings Equal


from typing import List, defaultdict

class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        
        d = defaultdict(int)

        for word in words:
            for w in word:
                d[w] += 1


        for k in d.keys():

            if d[k] % len(words) != 0:
                return False

        return True



words_1 = ["abc","aabc","bc"]
# Output: true
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.

words_2 = ["ab","a"]
# Output: false
# Explanation: It is impossible to make all the strings equal using the operation.

words_3 = ["bb","aacb","bbbca"]
# Output: false

print(Solution().makeEqual(words_1))
print(Solution().makeEqual(words_2))
print(Solution().makeEqual(words_3))




