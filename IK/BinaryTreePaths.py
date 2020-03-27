"""
https://leetcode.com/problems/binary-tree-paths/

257. Binary Tree Paths

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
from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    def helper(node):
      if node.left is None and node.right is None:
        result.append('->'.join(stack + [str(node.val)]))
        return

      stack.append(str(node.val))
      if node.left: helper(node.left)
      if node.right: helper(node.right)
      stack.pop()

    if not root: return []
    result = []
    stack = []
    helper(root)
    return result