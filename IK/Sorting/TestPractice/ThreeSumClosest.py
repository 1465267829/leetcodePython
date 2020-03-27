"""
https://leetcode.com/problems/3sum-closest/

16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from typing import *
import sys

class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for low in range(len(nums)-2):
      if low > 0 and nums[low] == nums[low-1]: continue
      mid, high = low+1, len(nums)-1
      while mid < high:
        current_sum = nums[low] + nums[mid] + nums[high]
        if current_sum < target:
          mid += 1
          while mid < high and nums[mid] == nums[mid-1]: mid += 1
        else:
          high -= 1
          while mid < high and nums[high] == nums[high+1]: high -= 1
      else:
        if abs(current_sum-target) < abs(result-target): result = current_sum
    return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
    # print(sol.threeSumClosest([0, 0, 0], 1))
