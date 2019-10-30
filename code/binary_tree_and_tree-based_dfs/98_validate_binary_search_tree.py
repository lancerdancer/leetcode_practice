"""
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    inorder traversal
    """
    def isValidBST(self, root: TreeNode) -> bool:
        self.last_val = None
        self.is_bst = True
        self.validate(root)
        return self.is_bst

    def validate(self, node):
        if node is None:
            return

        self.validate(node.left)
        if self.last_val is not None and self.last_val >= node.val:
            self.is_bst = False
            return

        self.last_val = node.val
        self.validate(node.right)


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)

    def validate(self, node, min_val, max_val):
        if node is None:
            return True

        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
            return False

        if not self.validate(node.left, min_val, node.val) or not self.validate(node.right, node.val, max_val):
            return False

        return True
