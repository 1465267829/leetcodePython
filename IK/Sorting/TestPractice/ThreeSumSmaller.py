"""
https://leetcode.com/problems/3sum-smaller/

259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""

from typing import *

class Solution:
  def floor(self, nums, start, end, target):
    low, high= start, end
    # result = []
    result = 0
    while low <= high:
      mid = low+((high-low)//2)
      if nums[mid] == target:
        # handle duplicates in the mid
        while mid > low and nums[mid] == nums[mid-1]: mid-=1
        # result = [i for i in range(start, mid)]
        result = mid-start
        return result
      elif target < nums[mid]:
        high = mid-1
      else:
        low = mid+1
    # result = [i for i in range(start, high+1)]
    result = high+1-start
    return result

  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = 0
    for i in range(0, len(nums)-2):
      for j in range(i+1, len(nums)):
        new_target = target-nums[i]-nums[j]
        floors = self.floor(nums, j+1, len(nums)-1, new_target)
        # result += len(floors)
        result += floors
        # for _ in floors: result += 1
    return result

if __name__ == '__main__':
    sol = Solution()
    # print(sol.threeSumSmaller([-2,0,1,3], 2))
    # print(sol.threeSumSmaller([-2,0,1,3], 2))
    # print(sol.threeSumSmaller([0, 1, 2, 3, 4, 5], 5))
    print(sol.threeSumSmaller([3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1], 3))
