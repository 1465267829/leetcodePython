"""
https://leetcode.com/problems/permutations-ii/

47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import *

"""
Following is easier and works

class Solution:

  def helper(self, current_nums, slate, result, k_slots, memo):
    if len(slate) == k_slots:
      result.append(slate[:])
      return
    for index, value in enumerate(current_nums):
      memo.add(tuple(slate))
      slate.append(value)
      if tuple(slate) not in memo:
        self.helper(current_nums[:index] + current_nums[index + 1:], slate, result, k_slots, memo)
      slate.pop()

  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    current_nums, slate, result, memo = nums, [], [], set()
    self.helper(current_nums, slate, result, len(nums), memo)
    return result
"""

# Following is better and works

class Solution:
  """
  Description of this is exactly the same as IK/Recursion/ClassExercises/PermutationWithoutRepetition.py
  Only difference is the logic to avoid duplicate permutations in event of nums having duplicate
  Logic is:
  At any given recursion when we iterate through list of available elements to put on slate
  we check if we have seen this element before. If we have then this means that the slate and
  new nums parameter for next recursion will yield a duplicate recursion subtree and hence
  duplicate permutation. So we skip such a duplicate item.
  Here we know that order of element in the list that is passed to next recursion doesn't
  matter as all the elements will be consumed from it eventually.
  """
  def helper(self, nums, index, slate, result, max_slots):
    if len(slate) == max_slots:
      result.append(slate[:])
      return

    if index == len(nums):
      return
    memo = set()
    for current_index in range(index, len(nums)):
      if nums[current_index] not in memo:
        slate.append(nums[current_index])
        # See https://www.youtube.com/watch?v=X-wGb5Mjhcc&feature=youtu.be
        nums[current_index], nums[index] = nums[index], nums[current_index]
        self.helper(nums, index + 1, slate, result, max_slots)
        nums[current_index], nums[index] = nums[index], nums[current_index]
        slate.pop()
        memo.add(nums[current_index])

  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    index, slate, result, max_slots = 0, [], [], len(nums)
    self.helper(nums, index, slate, result, max_slots)
    return result

if __name__ == '__main__':
  sol = Solution()
  print(sol.permuteUnique([1, 1, 2]))