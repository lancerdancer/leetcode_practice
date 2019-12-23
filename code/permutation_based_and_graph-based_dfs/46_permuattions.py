import unittest
from unittest import TestCase
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
    def permute(self, nums):
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

class Tests(TestCase):
    def setUp(self) -> None:
        self.target = Solution()

    def test_empty(self):
        self.assertEqual(self.target.permute([]), [])

    def test_simple(self):
        self.assertCountEqual(self.target.permute([1, 2, 3]), [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
])

if __name__ == '__main__':
    unittest.main()




