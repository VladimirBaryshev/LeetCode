# 79. Word Search
# https://leetcode.com/problems/word-search/


from typing import List

def exist(board: List[List[str]], word: str) -> bool:

    all_coords = dict()
    
    for i, n in enumerate(board):
        for j, m in enumerate(n):
            if m in all_coords.keys():
                all_coords[m].append((i, j))
            else:
                all_coords[m] = []
                all_coords[m].append((i, j))

    word_len = len(word)
    stack = [[[], [], word]]

    while stack:

        path, coords, word = stack.pop()

        if len(path) == word_len and len(word) == 0:
            if len(set(coords)) == len(coords):
                # print(path, coords, word, set(coords))
                return True

        for i, w in enumerate(word):

            if w not in all_coords.keys():
                return False

            for c in all_coords[w]:

                if len(coords) > 1 and coords[-2] != c:
                    x_1, y_1 = coords[-1]
                    x_2, y_2 = c

                    if abs(x_1 - x_2) + abs(y_1 - y_2) == 1:
                        stack.append([ path + [w], coords + [c], word[i+1:]])
                else:
                    stack.append([ path + [w], coords + [c], word[i+1:]])

                # print(stack)

    return False

board_0 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word_0 = "AB"
# Output: true

board_1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word_1 = "ABCCED"
# Output: true

board_2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word_2 = "SEE"
# Output: true

board_3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word_3 = "ABCB"
# Output: false

board_4 = [["a"]]
word_4 = "ab"
# Output: false

board_5 = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word_5 = "aaaaaaaaaaaa"
# Output: true

print(exist(board_0, word_0))
print(exist(board_1, word_1))
print(exist(board_2, word_2))
print(exist(board_3, word_3))
print(exist(board_4, word_4))
print(exist(board_5, word_5))

