"""
https://leetcode.com/problems/trapping-rain-water/


Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0

        idx_stack = []
        vol = 0

        for idx, h in enumerate(height):
            while idx_stack and h >= height[idx_stack[-1]]:
                ground_height = height[idx_stack.pop()]
                if len(idx_stack) == 0:
                    continue
                lo_idx = idx_stack[-1]
                water_line = min(h, height[lo_idx])
                vol += (water_line - ground_height) * (idx - lo_idx - 1)
            idx_stack.append(idx)

        return vol

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
