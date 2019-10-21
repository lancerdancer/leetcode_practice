"""
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    recursion
    """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        self.dfs(root, [str(root.val)], paths)

        return paths

    def dfs(self, node, current_path, paths):
        if node is None:
            return

        if node.left is None and node.right is None:
            paths.append("->".join(current_path))
            return

        if node.left:
            current_path.append(str(node.left.val))
            self.dfs(node.left, current_path, paths)
            current_path.pop()

        if node.right:
            current_path.append(str(node.right.val))
            self.dfs(node.right, current_path, paths)
            current_path.pop()
