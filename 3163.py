# 3163. String Compression III

class Solution:
    def compressedString(self, word: str) -> str:
        
        result = ""

        count = 1
        prev_i = word[0]
        for i in word[1:]:
            if prev_i == i:
                if count == 9:
                    result += str(count)
                    result += prev_i
                    count = 1
                else:
                    count += 1
            else:
                result += str(count)
                result += prev_i
                count = 1
                prev_i = i
        result += str(count)
        result += prev_i

        return result






word_1 = "abcde"
# Output: "1a1b1c1d1e"
# Explanation:
# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
# For each prefix, append "1" followed by the character to comp.


word_2 = "aaaaaaaaaaaaaabb"
# Output: "9a5a2b"
# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.

print(Solution().compressedString(word_1))
print(Solution().compressedString(word_2))