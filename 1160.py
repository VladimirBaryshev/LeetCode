# 1160. Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/


from typing import List, Counter
from collections import Counter



def match_word(string: str, char_counter: Counter) -> bool:

    word_counter = Counter(string)
    
    for char, count in word_counter.items():
        if char not in char_counter or count > char_counter[char]:
            return False

    return True


def sumGoodString(words: List[str], chars: str) -> int:
    
    returned_count = 0

    char_counter = Counter(chars)

    for word in words:
        if match_word(word, char_counter):
            returned_count += len(word)

    return returned_count 


words_1 = ["cat","bt","hat","tree"]
chars_1 = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

words_2 = ["hello","world","leetcode"]
chars_2 = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

print(sumGoodString(words_1, chars_1))
print(sumGoodString(words_2, chars_2))

