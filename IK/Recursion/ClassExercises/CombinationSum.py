"""
https://leetcode.com/problems/combination-sum/

39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import *


class Solution:
  def helper(self, candidates, target, slate, slate_sum, result):
    if slate_sum == target:
      result.add(tuple(sorted(slate[:])))
      return
    if slate_sum > target:
      return

    for element in candidates:
      slate.append(element)
      slate_sum += element
      self.helper(candidates, target, slate, slate_sum, result)
      slate_sum -= element
      slate.pop()

  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    slate, slate_sum, result = [], 0,  set()
    self.helper(candidates, target, slate, slate_sum, result)
    return result


if __name__ == '__main__':
  sol = Solution()
  # candidates, target = [2, 3, 6, 7], 7
  # candidates, target = [2,3,5], 8
  # candidates, target = [5,10,8,4,3,12,9], 27
  candidates, target = [2,5,2,1,2], 5
  res = sol.combinationSum(candidates, target)
  print(len(res), res)