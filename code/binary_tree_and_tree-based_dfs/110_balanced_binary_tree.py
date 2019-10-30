"""
https://leetcode.com/problems/balanced-binary-tree/


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.validate(root) != -sys.maxsize - 1

    def validate(self, node):
        if node is None:
            return -1

        left_h = self.validate(node.left)
        if left_h == -sys.maxsize - 1:  # pass error code up
            return -sys.maxsize - 1

        right_h = self.validate(node.right)
        if right_h == -sys.maxsize - 1:  # pass error code up
            return -sys.maxsize - 1

        if abs(left_h - right_h) > 1:
            return -sys.maxsize - 1
        else:
            return max(left_h, right_h) + 1
