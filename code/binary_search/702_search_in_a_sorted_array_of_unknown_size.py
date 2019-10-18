"""
https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1.
However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.



Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
"""


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        left, right = 0, 1
        # Find boundaries for binary search
        while reader.get(right) < target:
            left = right
            """
            Left shift: x << 1. The same as multiplying by 2: x * 2.
            Right shift: x >> 1. The same as dividing by 2: x / 2.
            """
            right <<= 1

        while left + 1 < right:
            mid = (left + right) // 2

            if reader.get(mid) == target:
                return mid

            if reader.get(mid) < target:
                left = mid
            else:
                right = mid

        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1
