"""
Implement BFS for an n-ary tree using generators in python
Implement BFS for an n-ary by implementing iterator interface
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

429. N-ary Tree Level Order Traversal
Medium

364

36

Favorite

Share
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:







We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import *
from IK.Trees.ClassExcercises.Tree import TreeNode
from queue import SimpleQueue

class Node:
  def __init__(self, val, children):
    self.val = val
    self.children = children

class Solution:
  @classmethod
  def level_order_iterator(cls, root):
    queue = SimpleQueue()
    queue.put(root)
    while not queue.empty():
      level_elements = []
      for _ in range(queue.qsize()):
        curr = queue.get()
        level_elements.append(curr.val)
        for child in curr.children: queue.put(child)
      yield level_elements

  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root: return None
    return [node for node in Solution.level_order_iterator(root)]


if __name__ == '__main__':
  _5 = Node(5, [])
  _6 = Node(6, [])
  _3 = Node(3, [_5, _6])
  _2 = Node(2, [])
  _4 = Node(4, [])
  root = Node(1, [_3, _2, _4])
  sol = Solution()
  print(sol.levelOrder(root))