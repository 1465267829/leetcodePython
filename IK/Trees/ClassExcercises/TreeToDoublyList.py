"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

http://cslibrary.stanford.edu/109/TreeListRecursion.html

426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:





We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.





Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

from typing import *
from IK.Trees.ClassExcercises.Tree import TreeNode


class Solution:

  @classmethod
  def inorder_iterator(cls, root):
    curr, stack = root, []
    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      yield curr
      curr = curr.right

  def treeToDoublyList(self, root: 'Node') -> 'Node':
    if not root: return root
    inorder_iter = Solution.inorder_iterator(root)
    head, prev = None, None
    while True:
      current = next(inorder_iter, None)
      if not head:
        head = current
      if not current:
        break
      if prev:
        prev.right = current
        current.left = prev
      prev = current
    head.left = prev
    prev.right = head
    return head


if __name__ == '__main__':
  sol = Solution()
  result = []
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(5)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  # for i in sol.inorder_iterator(root):
  #   if i is not None:
  #     result.append(i.val)
  # print(result)

  root = None
  head = sol.treeToDoublyList(root)
  pass
