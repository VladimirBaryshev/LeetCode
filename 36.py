# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

import collections


board_1 = [
	["5","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."],
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]
] # Output: true

board_2 = [
	["8","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."],
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]
] # Output: false


def map_(board):
	rows = collections.defaultdict(set)
	columns = collections.defaultdict(set)
	squares = collections.defaultdict(set)

	for r in range(9):
		for c in range(9):
			if board[r][c] == ".":
				continue

			if (

				board[r][c] in rows[r] or
				board[r][c] in columns[c] or
				board[r][c] in squares[(r//3, c//3)]

				):
				return False

			rows[r].add(board[r][c])
			columns[c].add(board[r][c])
			squares[(r//3, c//3)].add(board[r][c])

	return True

print(map_(board_1))
print(map_(board_2))









