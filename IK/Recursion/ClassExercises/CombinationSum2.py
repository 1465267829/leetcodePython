"""
https://leetcode.com/problems/combination-sum-ii/


40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import *


class Solution:

  def get_dup_count(self, nums, index):
    num, count = nums[index], 0
    for i in range(index, len(nums)):
      if nums[i] != nums[index]: break
      if nums[i] == nums[index]: count += 1
    return count

  def helper(self, nums, index, slate, result, target, slate_sum):
    if target == slate_sum:
      # we found the subset, return
      result.append(slate[:])
      return

    if target < slate_sum:
      # since all the numbers in nums are +ive and slate_sum already is
      # more than the target, backtrack
      return

    if index == len(nums):
      # base case, no more numbers to consume
      return

    # https://www.youtube.com/watch?v=X-wGb5Mjhcc&feature=youtu.be Time: 3:20:14
    dup_count = self.get_dup_count(nums, index)

    for i in range(0, dup_count+1):
      for j in range(0, i):
        slate.append(nums[index])
        slate_sum += nums[index]
      self.helper(nums, index + dup_count, slate, result, target, slate_sum)
      for j in range(0, i):
        slate_sum -= nums[index]
        slate.pop()

  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    index, slate, result, slate_sum = 0, [], [], 0
    self.helper(candidates, index, slate, result, target, slate_sum)
    return result


if __name__ == '__main__':
  sol = Solution()
  # nums, k = [2,3,6,7], 7
  nums, k = [2,5,2,1,2], 5
  print(sol.combinationSum2(nums, k))