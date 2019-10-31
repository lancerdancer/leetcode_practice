"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        # write your code here
        res = self.dfs(head)

        return res

    def dfs(self, head):

        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent

