# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/


from typing import List


'''
    Edges and constraints:
        len(strs) >= 1
        lowercase letters only
        each group consists same len of words
        each word is unique in strs


    Solution ideas:
    
        Worst case scenario O(strs[i]**2) + O(strs**2)
        
        create dict where key is string and list is value
        Iterate over strs
        sorted(strs[i]) 
         “”.join(result). Key created
        if key is absent and new key
        append origin strs[i] to list by corresponding key
'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:


    result = dict()

    for s in strs: # O(n)
        key = "".join(sorted(s)) # (Nlogn)
        if key not in result.keys():
            result[key] = []
        result[key].append(s)

    return result.values() #O(n) * O(nlogn)



strs_1 = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs_2 = [""]
# Output: [[""]]

strs_3 = ["a"]
# Output: [["a"]]
 
print(groupAnagram(strs_1)) 
print(groupAnagram(strs_2))
print(groupAnagram(strs_3))


