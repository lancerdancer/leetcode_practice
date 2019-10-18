"""
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

"""
from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = self.find_upper_closest(arr, x)
        left, right = pos - 1, pos
        result = deque([])

        while k > 0:
            if self.is_left_closer(arr, left, right, x):
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1

        return result

    def find_upper_closest(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                start = mid
            else:
                end = mid

        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end

        return len(arr)

    def is_left_closer(self, arr, left, right, x):
        if right >= len(arr):
            return True
        if left < 0:
            return False

        return x - arr[left] <= arr[right] - x