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

    for char in word:
        if char not in all_coords.keys():
            return False

    stack = [[[], [], 0, all_coords]]


    while stack:

        path, coords, idx, all_coords = stack.pop()

        if idx == len(word):

            return True

        else:

            for i, v in enumerate(all_coords[word[idx]]):


                updated_all_coords = all_coords.copy()

                updated_path = path.copy()
                updated_coords = coords.copy()

                pinned_out_coordinate = updated_all_coords[word[idx]][i]

                if len(updated_coords) > 0:
                    x_1, y_1 = updated_coords[-1]
                    x_2, y_2 = pinned_out_coordinate

                    if abs(x_1 - x_2) + abs(y_1 - y_2) != 1:
                        continue

                updated_coords.append(pinned_out_coordinate)
                not_pinned_out_coordinates = all_coords[word[idx]][:i] + all_coords[word[idx]][i+1:]
                updated_all_coords[word[idx]] = all_coords[word[idx]][:i] + all_coords[word[idx]][i+1:]
                updated_path.append(word[idx])

                stack.append([updated_path, updated_coords, idx+1, updated_all_coords])

        # for s in stack:
        #     print(s)
        # print('\n')

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

board_test = [["a","a"],["a","a"]]
word_test = "aaaa"
# Output: true

print(exist(board_0, word_0))
print(exist(board_1, word_1))
print(exist(board_2, word_2))
print(exist(board_3, word_3))
print(exist(board_4, word_4))
print(exist(board_5, word_5)) # TLE
print(exist(board_test, word_test))



