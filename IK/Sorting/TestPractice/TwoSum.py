"""
https://leetcode.com/problems/two-sum/

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import *

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    if not nums: return []
    mymap = {}
    for index, value in enumerate(nums):
      if value in mymap:
        return [mymap[value], index]
      else:
        mymap[target-value] = index


if __name__ == '__main__':
  sol = Solution()
  # nums, target = [2, 7, 11, 15], 9
  nums, target = [2, 2, 2, 7, 7, 7], 9
  print(sol.twoSumHashMap(nums, target))
  # print(sol.twoSumSort(nums, target))