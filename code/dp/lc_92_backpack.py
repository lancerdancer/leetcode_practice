"""
https://www.lintcode.com/problem/backpack/description

Given n items with size Ai, an integer m denotes the size of a backpack.
How full you can fill this backpack?

Example 1:
    Input:  [3,4,8,5], backpack size=10
    Output:  9

Example 2:
    Input:  [2,3,5,7], backpack size=12
    Output:  12
"""

class Solution:
    def backpack(self, m, A):
        n = len(A)
        dp = [False * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n+1):
            dp[i][0] = True
            for j in range(1, m+1):
                if j >= A[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
        return 0

class Solution1:
    """
    滚动数组优化
    """
    def backpack(self, m, A):
        n = len(A)
        dp = [False * (m + 1), False * (m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i % 2][0] = True
            for j in range(1, m+1):
                if j >= A[i - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[(i - 1) % 2][j - A[i - 1]]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]

        for i in range(m, -1, -1):
            if dp[n % 2][i]:
                return i
        return 0

