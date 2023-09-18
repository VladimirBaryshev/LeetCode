# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/


def firstUniqChar(string: str) -> int:

    d = dict()
    
    for s in string:
        
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
    
    for i in range(len(string)):
        if d[string[i]] == 1:
            return i
    
    return -1


s_1 = "leetcode" # Output: 0
s_2 = "loveleetcode" # Output: 2
s_3 = "aabb" # Output: -1

print(firstUniqChar(s_1))
print(firstUniqChar(s_2))
print(firstUniqChar(s_3))

