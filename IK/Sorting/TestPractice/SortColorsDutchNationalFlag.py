"""
Dutch National Flag Problem

https://leetcode.com/problems/sort-colors/

75. Sort Colors
Medium

2311

185

Add to List

Share
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

from typing import *


class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums: return nums
    red, white, blue = -1, 0, len(nums)
    while white < blue:
      if nums[white] == 1:
        white += 1
      elif nums[white] == 0:
        red += 1
        nums[white], nums[red] = nums[red], nums[white]
        white += 1
      else:
        blue -= 1
        nums[white], nums[blue] = nums[blue], nums[white]
    return nums


if __name__ == '__main__':
  sol = Solution()
  print(sol.sortColors([2,0,2,1,1,0]))