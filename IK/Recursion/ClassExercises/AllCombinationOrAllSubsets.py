"""
https://leetcode.com/problems/subsets/

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import *


class Solution:
  def helper(self, nums, nums_index, slate, result):
    if nums_index == len(nums):
      result.append(slate[:])
      return
    # exclude
    self.helper(nums, nums_index + 1, slate, result)
    # include
    slate.append(nums[nums_index])
    self.helper(nums, nums_index + 1, slate, result)
    slate.pop()
    return

  def subsets(self, nums: List[int]) -> List[List[int]]:
    result, slate = [], []
    self.helper(nums, 0, slate, result)
    return result


if __name__ == '__main__':
  nums = [2,2,2]
  sol = Solution()
  print(sol.subsets(nums))

