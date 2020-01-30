"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -sys.maxsize - 1
        self.helper(root)
        return self.max_sum

    def helper(self, node):
        """
        return the maximum pathsum passing the node
        """
        if node is None:
            return 0

        left_sum = self.helper(node.left)  # sum >= 0 guarenteed
        right_sum = self.helper(node.right)

        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
        return max(node.val + left_sum, node.val + right_sum, 0)
