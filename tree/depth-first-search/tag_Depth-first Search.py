'''
https://leetcode.com/problemset/algorithms/?topicSlugs=depth-first-search
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num

'''
https://leetcode.com/problems/nested-list-weight-sum-ii/
364. Nested List Weight Sum II
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red = 0
    blue = len(nums) - 1
    for current in range(len(nums)):
      if current >= blue:
        break
      elif nums[current] == 0:
        nums[red], nums[current] = nums[current], nums[red]
        red += 1
      elif nums[current] == 2:
        nums[blue], nums[current] = nums[current], nums[blue]
        blue -= 1
    return nums

  def sortColors0(self, nums):
    zero_write_index = 0
    one_write_index = 0
    two_write_index = len(nums) - 1

    while one_write_index <= two_write_index:
      if nums[one_write_index] == 0:
        nums[one_write_index], nums[zero_write_index]  = nums[zero_write_index], nums[one_write_index]
        zero_write_index += 1
      elif nums[one_write_index] == 1:
        # nums[one_write_index], nums[one_write_index] = nums[one_write_index], nums[one_write_index] # moot
        pass
      else:
        nums[one_write_index], nums[two_write_index] = nums[two_write_index], nums[one_write_index]
        two_write_index -= 1
      one_write_index += 1
    return nums

  def sort_less_equal_greater(self, nums, pivot):
    less_write_index = 0
    equal_write_index = 0
    greater_write_index = len(nums) - 1

    while equal_write_index <= greater_write_index:
      if nums[equal_write_index] < pivot:
        nums[equal_write_index], nums[less_write_index]  = nums[less_write_index], nums[equal_write_index]
        less_write_index += 1
      elif nums[equal_write_index] == pivot:
        # nums[one_write_index], nums[one_write_index] = nums[one_write_index], nums[one_write_index] # moot
        pass
      else:
        nums[equal_write_index], nums[greater_write_index] = nums[greater_write_index], nums[equal_write_index]
        greater_write_index -= 1
      equal_write_index += 1
    return nums

if __name__ == '__main__':
  sol = Solution()
  print sol.sortColors([2,0,2,1,1,0])
  print sol.sortColors0([2,0,2,1,1,0])
  print sol.sort_less_equal_greater([20, 4, 2, 3, 4, 22, 21, 23, 24], 20)