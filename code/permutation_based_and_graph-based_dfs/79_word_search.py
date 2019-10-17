"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(board, x, y, word, index):
            if index == len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

            board[x][y] = '*'
            res = False
            for dx, dy in DIRECTIONS:
                res = res or dfs(board, x + dx, y + dy, word, index + 1)
            board[x][y] = word[index]
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(board, r, c, word, 0):
                        return True
