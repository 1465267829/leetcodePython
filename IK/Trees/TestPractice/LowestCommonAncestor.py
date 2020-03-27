"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

  def __init__(self):
    self.ans = None

  def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
      return False
    # send both values to both the subtrees
    left = self.helper(root.left, p, q)
    right = self.helper(root.right, p, q)
    # check if root is one of p or q
    mid = True if root.val == p.val or root.val == q.val else False
    if left is True and right is True:
      # we found either one of p or q in either on of the subtrees
      # then root must be the LCA
      self.ans = root
      return True
    if left is True and mid is True:
      # root is one of either p and q and other one is found left subtree
      # then root must be the LCA
      self.ans = root
      return True
    if right is True and mid is True:
      # root is one of either p and q and other one is found right subtree
      # then root must be the LCA
      self.ans = root
      return True
    if left is True or right is True or mid is True:
      # we found at at least one of p or q among root and left and right subtree
      # return True
      return True
    # root neither is p or q or neither p or q are in any subtrees
    return False

  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    self.helper(root, p, q)
    return self.ans


if __name__ == '__main__':
  sol = Solution()