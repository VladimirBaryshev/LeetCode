# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/



def reverseWords(string: str) -> str:

    string = string.strip().split()
    string.reverse()

    return " ".join(string)



s_1 = "the sky is blue" # Output: "blue is sky the"
s_2 = "  hello world  " # Output: "world hello"
s_3 = "a good   example" # Output: "example good a"


print(reverseWords(s_1))
print(reverseWords(s_2))
print(reverseWords(s_3))