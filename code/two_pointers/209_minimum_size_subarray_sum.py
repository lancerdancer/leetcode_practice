"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s,
 find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        j = 0
        current_sum = 0
        min_size = sys.maxsize

        for i in range(len(nums)):
            while j < len(nums) and current_sum < s:
                current_sum += nums[j]
                j += 1

            if current_sum >= s:
                min_size = min(j - i, min_size)
            current_sum -= nums[i]

        if min_size == sys.maxsize:
            return 0

        return min_size
