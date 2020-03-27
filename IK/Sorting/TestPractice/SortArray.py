"""
912. Sort an Array

https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""

from random import randrange
from typing import *


class Solution:
  def lomuto_partitioning(self, nums, start, end):
    """
    Important:
    1. In this scheme, the pivot's final location in sorted array is at the index that was returned.
    2. ELements between indexes 'start' and 'less-1' [both inclusive] less than the element at the 'less' index.
    3. Elements between indexes 'less' and 'end' [both inclusive] are more then or equal to element at the 'less' index.
    4. 'less' index after the partitioning is the pivot index and is returned.
    5. Elements between 'start' and 'less-1' [both inclusive] are unsorted.
    6. Elements between 'less' and 'end' [both inclusive] are unsorted.
    7. Next two segments that the main quick sort algorithm recurs on are (lo..p-1) and (p+1..hi)
    """
    if start >= end: return nums
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

  def hoare_partitioning(self, nums, start, end):
    """
    From quick sort wiki
    Hoare's scheme is more efficient than Lomuto's partition scheme because it does three times fewer swaps on average,
    and it creates efficient partitions even when all values are equal.

    Important:
    1. In this scheme, the pivot's final location in sorted array is not necessarily at the index that was returned.
    2. ELements between indexes 'start' and 'right' [both inclusive] less than or equal to the element at the 'right' index.
    3. Elements between indexes 'right' and 'end' [both inclusive] are more than the element at the 'right' index.
    4. 'right' index after the partitioning is the pivot index and is returned.
    5. Elements between 'start' and 'right' [both inclusive] are unsorted.
    6. Elements between 'right+1' and 'end' [both inclusive] are unsorted.
    7. Next two segments that the main quick sort algorithm recurs on are (lo..p) and (p+1..hi)
    """
    random_index = randrange(start, end)
    pivot = nums[random_index]
    left, right = start, end
    while True:
      while nums[left] < pivot : left += 1
      while nums[right] > pivot : right -= 1
      if left >= right: break
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
    return right

  def helper(self, nums, start, end):
    if start < end:
      # hoare paritioning
      pivot_index = self.hoare_partitioning(nums, start, end)
      # note the split as compared to lomuto's partition
      self.helper(nums, start, pivot_index)
      self.helper(nums, pivot_index+1, end)

      # lomuto's partitioning
      # pivot_index = self.lomuto_partitioning(nums, start, end)
      # self.helper(nums, start, pivot_index-1)
      # self.helper(nums, pivot_index+1, end)
    return nums

  def sortArray(self, nums: List[int]) -> List[int]:
    return self.helper(nums, 0, len(nums)-1)


if __name__ == '__main__':
    sol = Solution()
    # nums = [5,2,3,1]
    # nums = [5, 1, 1, 2, 0, 0]
    # nums = [0, 5, 1, 1, 2, 0, 0]
    # nums = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9]
    nums = [9, 8, 7, 7, 5, 5, 1, 2, 3] # [1, 2, 3, 5, 5, 7, 7, 8, 9]

    print(sol.sortArray(nums))