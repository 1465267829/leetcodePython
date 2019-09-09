# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
'''
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return 0

    current = root
    queue = [current]
    max_depth = 0

    while queue:
      max_depth += 1
      for _ in xrange(len(queue)):
        current = queue.pop(0)
        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)
    return max_depth
