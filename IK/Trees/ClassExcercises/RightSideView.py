"""
https://leetcode.com/problems/binary-tree-right-side-view/

199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""
# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
      result = []
      if not root:
        return result
      curr = root
      queue = []
      queue.append(curr)
      while queue:
        current_level = None
        for _ in range(len(queue)):
          curr = queue.pop(0)
          current_level = curr.val
          if curr.left: queue.append(curr.left)
          if curr.right: queue.append(curr.right)
        result.append(current_level)
      return result
