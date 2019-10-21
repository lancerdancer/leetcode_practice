"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    last_node = None

    def flatten(self, root):
        self.helper(root)

    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return None

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        if right_last is not None:
            return right_last

        if left_last is not None:
            return left_last

        return root

    def flatten1(self, root):
        """
        another version
        """
        while root:
            if root.left:
                self.flatten(root.left)
                tail = root.left
                while tail.right:
                    tail = tail.right
                tail.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
