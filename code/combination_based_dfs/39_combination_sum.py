"""
https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        results = []
        self.dfs(candidates, target, [], results, size, 0)
        return results

    def dfs(self, candidates, target, path, results, size, start):
        if target == 0:
            results.append(path[:])
            return

        for i in range(start, size):
            current = candidates[i]
            if current > target:
                break

            path.append(current)
            self.dfs(candidates, target-current, path, results, size, i)
            path.pop()
