"""
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        self.dfs(nums, [], result)
        return result


    def dfs(self, nums, path, result):
        if len(nums) <= 0:
            result.append(path[:])
            return

        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i+1:], path, result)
            path.pop()





