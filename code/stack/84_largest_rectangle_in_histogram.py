"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indices_stack = []
        area = 0
        for index, height in enumerate(heights + [0]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1
                width = index - left_index - 1
                area = max(area, width * heights[popped_index])

            indices_stack.append(index)

        return area
