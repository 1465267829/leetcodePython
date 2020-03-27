"""

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
from typing import *
from IK.Trees.ClassExcercises.Tree import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from IK.Trees.ClassExcercises.Tree import TreeNode


class Solution:

  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def helper(nums, start, end):
      if start > end: return None
      mid = start + ((end-start)//2)
      root = TreeNode(nums[mid])
      root.left = helper(nums, start, mid-1)
      root.right = helper(nums, mid+1, end)
      return root
    if not nums: return None
    return helper(nums, 0, len(nums)-1)


if __name__ == '__main__':
  sol = Solution()
  nums = [-10,-3,0,5,9]
  root = sol.sortedArrayToBST(nums)