"""
https://leetcode.com/problems/combinations/

77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
from typing import *


class Solution:
  """
  Implements C(N,K)
  1.  Generate all combinations/subsets given a set/lits of numbers
  2.  Start with slate as empty
  3. Always consider the 0th element in nums to either, exclude it or include it
  4. Exclusion means nothing is added to slate and the 0th element is removed from nums
  4. Inclusion means 0th element is added to slate and the 0th element is removed from nums
  """
  def helper(self, nums, index, slate, result, k):
    if len(slate) == k:
      result.append(slate[:])
      return

    if len(nums) == index:
      return

    # exclude
    self.helper(nums, index+1, slate, result, k)
    # include
    slate.append(nums[index])
    self.helper(nums, index+1, slate, result, k)
    slate.pop()

  def combine(self, n: int, k: int) -> List[List[int]]:
    nums, index, slate, result = [i for i in range(1, n+1)], 0, [], []
    self.helper(nums, index, slate, result, k)
    return result


if __name__ == '__main__':
  sol = Solution()
  res = sol.combine(4, 2)
  print(len(res), res)