"""
https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

"""


class Solution:
    """
    Backtrack without memoization
    100ms
    beat 44.52%
    """
    def partition(self, s):
        if not s:
            return []

        result = []
        self.dfs(s, [], result)
        return result

    def dfs(self, s, path, result):
        if s == "":
            result.append(path[:])
            return

        for i in range(len(s)):
            prefix = s[:i + 1]
            if prefix != prefix[::-1]:
                continue

            path.append(prefix)
            self.dfs(s[i+1:], path, result)
            path.pop()


class Solution1:
    """
    With memoization
    76ms
    beat 89.33%
    """
    def partition(self, s):
        return self.dfs(s, {})

    def dfs(self, s, memo):
        if s == "":
            return []

        if s in memo:
            return memo[s]

        partitions = []
        for i in range(len(s) - 1):
            prefix = s[:i + 1]
            if prefix != prefix[::-1]:
                continue

            sub_partitions = self.dfs(s[i + 1:], memo)
            for p in sub_partitions:
                partitions.append([prefix] + p)

        if s == s[::-1]:
            partitions.append([s])

        memo[s] = partitions
        return partitions





