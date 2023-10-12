# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie:

    def __init__(self):
        
        self.trie = dict()

    def insert(self, word: str) -> None:

        cur_dict = self.trie

        for c in word:

            if c not in cur_dict:
                cur_dict[c] = dict()

            cur_dict = cur_dict[c]

        cur_dict['END'] = True


    def search(self, word: str) -> bool:
        
        cur_dict = self.trie

        for c in word:

            if c not in cur_dict:
                return False

            cur_dict = cur_dict[c]

        return 'END' in cur_dict


    def startsWith(self, prefix: str) -> bool:
        
        cur_dict = self.trie

        for c in prefix:

            if c not in cur_dict:
                return False

            cur_dict = cur_dict[c]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output [null, null, true, false, true, null, true]

obj = Trie()
obj.insert("apple") # None
print(obj.search("apple")) # True
print(obj.search("app")) # False
print(obj.startsWith("app")) # True
print(obj.insert("app")) # None
print(obj.search("app")) # True


# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True




