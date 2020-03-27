"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


from random import randrange
from typing import *


# class Solution:
#   def lomuto_partition(self, nums: List[int], start: int, end: int) -> int:
#     # we use 1st element as pivot here. It could be randranged
#     less = start
#     for more in range(start+1, end+1):
#       if nums[more] <= nums[start]:
#         less += 1
#         nums[less], nums[more] = nums[more], nums[less]
#     nums[less], nums[start] = nums[start], nums[less]
#     return less
#
#   def findKthLargest(self, nums: List[int], k: int) -> int:
#     # kth largest means we are looking for 2nd index from
#     # right in a sorted array.
#     # last index in len(nums)-1 which is 1st largest
#     # kth largest is len(nums)-k
#     index_kth_largest = len(nums)-k
#     start, end = 0, len(nums)-1
#
#     while start <= end:
#       pivot_index = self.lomuto_partition(nums, start, end)
#       if index_kth_largest == pivot_index:
#         return nums[pivot_index]
#       elif index_kth_largest < pivot_index:
#         end = pivot_index-1
#       else:
#         start = pivot_index+1
#     return -1


class Solution:
  def lomuto_partitioning(self, nums, start, end):
    if start == end: return start
    pivot = randrange(start, end)
    pivot_num = nums[pivot]
    nums[pivot], nums[start] = nums[start], nums[pivot]
    less = start
    for more in range(less, end + 1):
      if nums[more] < pivot_num:
        less += 1
        nums[less], nums[more] = nums[more], nums[less]
    nums[start], nums[less] = nums[less], nums[start]
    return less

  def findKthLargest(self, nums: List[int], k: int) -> int:
    # kth largest means we are looking for 2nd index from
    # right in a sorted array.
    # last index in len(nums)-1 which is 1st largest
    # kth largest is len(nums)-k
    index_kth_largest = len(nums)-k
    start, end = 0, len(nums)-1

    while start <= end:
      if start == end: return nums[start]

      pivot_index = self.lomuto_partition(nums, start, end)
      if index_kth_largest <= pivot_index:
        end = pivot_index
      else:
        start = pivot_index + 1


if __name__ == '__main__':
  # nums, k = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4 # 4
  nums, k = [3, 2, 1, 5, 6, 4], 2 # 5

  sol = Solution()
  # print(sol.kthlargestPriorityQueue(nums, k))
  # print(sol.kthLargestQuickSelection(nums, k))
  print(sol.findKthLargest(nums, k))
