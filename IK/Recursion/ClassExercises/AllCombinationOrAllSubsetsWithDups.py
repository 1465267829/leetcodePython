"""
https://leetcode.com/problems/subsets-ii/

90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

from typing import *

"""
Following is better and works

class Solution:

  def helper(self, S, i, slate, result):
    if i == len(S):
      result.append(slate[:])
    else:
      count = 1
      j = i + 1
      while j <= len(S) - 1 and S[j] == S[i]:
        count += 1
        j += 1

      for copies in range(0, count + 1):
        for op in range(copies):
          slate.append(S[i])
        self.helper(S, i + count, slate, result)
        for op in range(copies):
          slate.pop()
    return

  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result, slate = [], []
    nums.sort()
    self.helper(nums,0, slate, result)
    return result
"""

# Following is easier and works


class Solution:

  def get_dup_count(self, nums, index):
    num, count = nums[index], 0
    for i in range(index, len(nums)):
      if nums[i] != nums[index]: break
      if nums[i] == nums[index]: count += 1
    return count

  def helper(self, nums, index, slate, result):
    if index == len(nums):
      result.append(slate[:])
      return
    # https://www.youtube.com/watch?v=X-wGb5Mjhcc&feature=youtu.be Time: 3:20:14
    dup_count = self.get_dup_count(nums, index)

    for i in range(0, dup_count+1):
      for j in range(0, i): slate.append(nums[index])
      self.helper(nums, index + dup_count, slate, result)
      for j in range(0, i): slate.pop()

  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    index, slate, result = 0, [], []
    self.helper(nums, index, slate, result)
    return result


if __name__ == '__main__':
  nums = [2,2,2,4]
  # nums = [3, 3, 4]
  # nums = [1, 1, 1, 2]
  # nums = [1, 2, 2]
  sol = Solution()
  print(sol.subsetsWithDup(nums))

