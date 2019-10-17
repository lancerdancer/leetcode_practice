"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 1 or n < k:
            return []

        result = []
        self.dfs(n, k, 1, [], result)
        return result

    def dfs(self, n, k, start, path, result):
        if k == 0:
            result.append(path[:])
            return

        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, k-1, i+1, path, result)
            path.pop()
