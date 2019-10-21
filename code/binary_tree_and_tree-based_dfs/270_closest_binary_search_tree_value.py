"""
https://leetcode.com/problems/closest-binary-search-tree-value/


Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None

        upper = root.val
        lower = root.val

        node = root

        while node:
            if node.val > target:
                upper = node.val
                node = node.left

            elif node.val < target:
                lower = node.val
                node = node.right

            else:
                return node.val

        if abs(upper - target) < abs(lower - target):
            return upper

        return lower