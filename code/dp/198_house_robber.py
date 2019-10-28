"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        f = [0] * 2
        f[0], f[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            f[i % 2] = max(f[(i - 1) % 2], f[(i - 2) % 2] + nums[i])  # 滚动数组优化

        return f[(len(nums) - 1) % 2]


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        if n <= 2:
            return max(nums)

        # f[i] is the max amount at house nums[i]
        f = [0] * n  # 没有滚动数组优化， 空间O(n)
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])

        return f[n - 1]

