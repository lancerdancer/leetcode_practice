"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        # Sort for eliminate duplicates
        nums.sort()
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        if len(nums) <= 0:
            result.append(path[:])
            return

        for i in range(len(nums)):
            # if the number is the same as previous, then the combination has already been generated. Why?
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            self.dfs(nums[:i] + nums[i+1:], path, result)
            path.pop()
