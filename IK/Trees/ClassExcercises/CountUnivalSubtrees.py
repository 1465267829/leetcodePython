"""

https://leetcode.com/problems/count-univalue-subtrees/
https://www.geeksforgeeks.org/find-count-of-singly-subtrees/

250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

"""
from typing import *

# Definition for a binary tree node.


class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Counter:
  def __init__(self):
    self.count = 0


class Solution:
  def isUnival(self, node, counter):
    if node is None: return True

    is_left_uvt = self.isUnival(node.left, counter)
    is_right_uvt = self.isUnival(node.right, counter)
    if not is_left_uvt or not is_right_uvt:
      return False
    if node.left and node.left.val != node.val:
      return False
    if node.right and node.right.val != node.val:
      return False
    counter.count += 1
    return True

  def countUnivalSubtrees(self, root: TreeNode) -> int:
    counter = Counter()
    self.isUnival(root, counter)
    return counter.count


if __name__ == '__main__':
  # nums = [5,1,5,5,5,None,5]
  # root = generate_tree(nums)

  # root = TreeNode(5)
  # root.left = TreeNode(1)
  # root.right = TreeNode(5)
  # root.left.left = TreeNode(5)
  # root.left.right = TreeNode(5)
  # root.right.right = TreeNode(5)

  root = TreeNode(5)
  root.left = TreeNode(5)
  root.right = TreeNode(5)
  root.left.left = TreeNode(5)
  root.left.right = TreeNode(5)
  root.right.right = TreeNode(5)

  sol = Solution()
  print(sol.countUnivalSubtrees(root))
