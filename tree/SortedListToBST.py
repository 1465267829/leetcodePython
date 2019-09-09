'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num

class SolutionSortedArrayToBST(object):
    def sortedArrayToBST(self, nums):
      if not nums: return None
      mid = len(nums) // 2
      root = TreeNode(nums[mid])
      root.left = self.sortedArrayToBST(nums[:mid])
      root.right = self.sortedArrayToBST(nums[mid + 1:])
      return root

if __name__ == '__main__':
  sol = SolutionSortedArrayToBST()
  root = sol.sortedArrayToBST([-10,-3,0,5,9])
  pass