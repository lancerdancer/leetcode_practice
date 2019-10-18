"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid

        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]
