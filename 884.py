# 884. Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/


from typing import List

class Solution:

    def uncommonFromSentences(self, A : str, B : str) -> List[str]:
        
        word_counter = dict()

        for word in A.split()+B.split(): 
            if word in word_counter.keys(): 
                word_counter[word] += 1
            else:
                word_counter[word] = 1
                
        return [k for k,v in word_counter.items() if v == 1]
