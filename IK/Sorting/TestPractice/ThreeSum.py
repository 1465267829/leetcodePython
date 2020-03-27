"""
https://leetcode.com/problems/3sum/

15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import *

# class Solution:
#   def threeSumSort(self, nums: List[int], target: int) -> List[List[int]]:
#     if not nums: return []
#     nums.sort()
#     result = []
#     for left in range(len(nums)-2):
#       if left > 0 and nums[left] == nums[left-1]: continue
#       middle, right = left + 1, len(nums) - 1
#       while middle < right:
#         current_sum = nums[left] + nums[middle] + nums[right]
#         if current_sum == target:
#           result.append([nums[left], nums[middle], nums[right]])
#           middle += 1
#           while middle < right and nums[middle] == nums[middle-1]: middle += 1
#           right -= 1
#           while right > middle and nums[right] == nums[right+1]: right -= 1
#         elif current_sum < target:
#           middle += 1
#         else:
#           right -= 1
#     return result
#
#   def threeSumSet(self, nums: List[int], target: int) -> List[List[int]]:
#     if not nums: return []
#     nums.sort()
#     # set simplifies dup handling
#     result = set()
#     for left in range(len(nums)-2):
#       middle, right = left + 1, len(nums) - 1
#       while middle < right:
#         current_sum = nums[left] + nums[middle] + nums[right]
#         if current_sum == target:
#           result.add((nums[left], nums[middle], nums[right]))
#           middle += 1
#           right -= 1
#         elif current_sum < target:
#           middle += 1
#         else:
#           right -= 1
#     return list(result)
#
#   def threeSumRecursive(self, nums: List[int], target: int) -> List[List[int]]:
#     def twoSumSort(nums: List[int], start_index: int, end_index: int, target: int) -> List[List[int]]:
#       left, right = start_index, end_index
#       result = []
#       while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#           result.append([nums[left], nums[right]])
#           while left < right and nums[left + 1] == nums[left]: left += 1
#           while left < right and nums[right - 1] == nums[right]: right -= 1
#           left += 1
#           right -= 1
#         elif current_sum < target:
#           left += 1
#         else:
#           right -= 1
#       return result
#
#     if not nums: return []
#     nums.sort()
#     result = []
#     for left in range(len(nums)-2):
#       if left > 0 and nums[left] == nums[left-1]: continue
#       two_sum_result = twoSumSort(nums, left+1, len(nums)-1, target-nums[left])
#       for item in two_sum_result:
#         result.append([nums[left]] + item)
#     return result
#
#   def threeSumRecursiveN(self, nums, target):
#     def findNsum(nums, target, N, result, results):
#       if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
#           return
#       if N == 2:  # two pointers solve sorted 2-sum problem
#         l, r = 0, len(nums)-1
#         while l < r:
#           s = nums[l] + nums[r]
#           if s == target:
#             results.append(result + [nums[l], nums[r]])
#             l += 1
#             while l < r and nums[l] == nums[l-1]:
#                 l += 1
#           elif s < target:
#             l += 1
#           else:
#             r -= 1
#       else:  # recursively reduce N
#         for i in range(len(nums)-N+1):
#           if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#             findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
#     nums.sort_top_down_divide_and_conquer()
#     result, results = [], []
#     findNsum(sorted(nums), target, 3, result, results)
#     return results

class Solution:
  def two_sum(self, nums, start, end, target):
    if start >= end: return []
    result = []
    while start < end:
      temp = nums[start] + nums[end]
      if temp == target:
        result.append([nums[start], nums[end]])
        while start + 1 < end and nums[start + 1] == nums[start]: start += 1
        start += 1
        while end - 1 > start and nums[end - 1] == nums[end]: end -= 1
        end -= 1
      elif temp < target:
        while start + 1 < end and nums[start + 1] == nums[start]: start += 1
        start += 1
      else:
        while end - 1 > start and nums[end - 1] == nums[end]: end -= 1
        end -= 1
    return result

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3: return []
    nums.sort()
    result = []
    i = 0
    while 0 <= i <= len(nums) - 3:
      res_two = self.two_sum(nums, i + 1, len(nums) - 1, 0 - nums[i])
      for item in res_two:
        result.append([nums[i]] + item)
      # slid to avoid processing dups
      while (0 < i + 1 <= len(nums) - 3) and nums[i + 1] == nums[i]: i += 1
      i += 1
    return result


if __name__ == '__main__':
  sol = Solution()
  nums, target = [-1, 0, 1, 2, -1, -4], 0
  # nums, target = [1, 0, -1, 0, -2, 2], 0
  # print(sol.threeSumSort(nums, target))
  # print(sol.threeSumSet(nums, target))
  # print(sol.threeSumRecursive(nums, target))
  # print(sol.threeSumRecursiveN(nums, target))
  print(sol.threeSum(nums))
