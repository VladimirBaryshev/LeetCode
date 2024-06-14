# 1023. Camelcase Matching
# https://leetcode.com/problems/camelcase-matching/description/


from typing import List

class Solution:

    def map_query(self, query, pattern):

        p_pointer = 0

        for i, char in enumerate(query):
    
            if p_pointer < len(pattern) and query[i] == pattern[p_pointer]:
                p_pointer += 1
            elif query[i].isupper(): #Coop, Cgfbfcoop
                return False #


        return p_pointer == len(pattern)
            
    

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.map_query(i, pattern) for i in queries]
        