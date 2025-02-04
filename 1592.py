# 1592. Rearrange Spaces Between Words

class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        words = text.split()
        space_count = len([i for i in text if i == ' '])
        words_count = len(words)

        if words_count == 1:
            return words[0] + ' '*space_count

        else:
            q, r = divmod(space_count, words_count-1)
            return (' '*q).join(words) + (' '*r)


text_1 = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. 
# We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

text_2 = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. 
# We place this extra space at the end of the string.        

print(Solution().reorderSpaces(text_1))
print(Solution().reorderSpaces(text_2))
# print(Solution().reorderSpaces("a"))
print(Solution().reorderSpaces("  hello"))