"""
https://leetcode.com/problems/inorder-successor-in-bst/
285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Note:
If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""

from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    # look at   def find_successor(self, key): in BinarySearchTree.py for explanation
    prev, foo, curr = None, None, root
    while curr:
      if p.val == curr.val:
        break
      elif p.val < curr.val:
        foo = curr
        prev = curr
        curr = curr.left
      else:
        prev = curr
        curr = curr.right
    if curr.right:
      curr = curr.right
      while curr.left:
        curr = curr.left
      return curr
    else:
      if not prev:
        return None
      else:
        if prev.left == curr:
          return prev
        if prev.right == curr:
          return foo