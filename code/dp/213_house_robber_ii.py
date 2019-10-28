"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""


class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    # version1 classical solution
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        f = [0 for _ in range(len(nums))]
        max_res = 0
        # case1 do not have the last elem
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])
        max_res = max(max_res, f[len(nums) - 2])

        # case2 do not have the first elem
        f[1], f[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])
        max_res = max(max_res, f[len(nums) - 1])

        return max_res

    # version2 rolling array %3
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        f = [0 for _ in range(3)]
        max_res = 0
        # case1 do not have the last elem
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + nums[i])
        max_res = max(max_res, f[(len(nums) - 2) % 3])

        # case2 do not have the first elem
        f[1], f[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + nums[i])
        max_res = max(max_res, f[(len(nums) - 1) % 3])

        return max_res

    # version3 rolling array %2
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        f = [0 for _ in range(2)]
        max_res = 0
        # case1 do not have the last elem
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            f[i % 2] = max(f[(i - 1) % 2], f[(i - 2) % 2] + nums[i])
        max_res = max(max_res, f[(len(nums) - 2) % 2])

        # case2 do not have the first elem
        # ATTENTION! CHANGE!
        f[1], f[0] = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            f[i % 2] = max(f[(i - 1) % 2], f[(i - 2) % 2] + nums[i])
        max_res = max(max_res, f[(len(nums) - 1) % 2])

        return max_res