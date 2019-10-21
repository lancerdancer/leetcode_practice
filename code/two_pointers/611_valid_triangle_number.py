"""
https://leetcode.com/problems/valid-triangle-number/

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        triangle_number = 0
        for i in range(2, len(nums)):
            triangle_number += self.find_valid_pairs(nums, i)

        return triangle_number

    def find_valid_pairs(self, nums, index):
        """
        nums[index] is always larger.
        It is guarentted that num[index] + nums[right] > nums[left]
        and num[index] + nums[left] > nums[right]
        """
        left, right = 0, index - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > nums[index]:
                count += right - left
                right -= 1
            else:
                left += 1

        return count
