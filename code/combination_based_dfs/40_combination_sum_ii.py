"""
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, [], results, size)

        return results


    def dfs(self, candidates, target, start, path, results, size):
        if target == 0:
            results.append(path[:]) # deep copy
            return

        for i in range(start, size):
            current = candidates[i]
            if current > target:
                break

            if i != start and candidates[i] == candidates[i-1]:
                continue

            path.append(current)
            self.dfs(candidates, target-current, i+1, path, results, size)
            path.pop()
