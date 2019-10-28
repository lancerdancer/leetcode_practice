"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return
        n = len(grid[0])
        if not n:
            return

        dp = [[0] * n, [0] * n]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i % 2][j] = grid[i][j] + dp[(i - 1) % 2][j]
                else:
                    dp[i % 2][j] = grid[i][j] + min(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

        return dp[(m - 1) % 2][n - 1]
