"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


class TreeNode:
  def __init__(self, node_value):
      self.val = node_value
      self.left_ptr = None
      self.right_ptr = None


def inorder_recursive_generator(root):
  if root:
    yield from inorder_recursive_generator(root.left_ptr)
    yield root.val
    yield from inorder_recursive_generator(root.right_ptr)


def kth_smallest_element(root, k):
  iter = inorder_recursive_generator(root)
  for i in range(k-1):
    next(iter)
  return next(iter)


if __name__ == '__main__':
  root = TreeNode(2)
  root.left_ptr = TreeNode(1)
  root.right_ptr = TreeNode(3)
  print(kth_smallest_element(root, 2))

