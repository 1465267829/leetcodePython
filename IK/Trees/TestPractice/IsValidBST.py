"""
https://leetcode.com/problems/validate-binary-search-tree/

98. Validate Binary Search Tree
Medium

2610

381

Favorite

Share
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
from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, root, start, end):
      if not root:
        return True
      if start < root.val < end and self.helper(root.left, start, root.val) and self.helper(root.right, root.val, end):
        return True
      return False

    def isValidBST(self, root: TreeNode) -> bool:
      return self.helper(root, float('-inf'), float('inf'))


if __name__ == '__main__':
  # root = TreeNode(2)
  # root.left = TreeNode(1)
  # root.right  = TreeNode(3)

  root = TreeNode(5)
  root.left = TreeNode(1)
  root.right = TreeNode(4)
  root.right.left = TreeNode(3)
  root.right.right = TreeNode(6)

  sol = Solution()
  print(sol.isValidBST(root))


