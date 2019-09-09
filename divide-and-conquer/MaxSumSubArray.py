'''
https://leetcode.com/problems/maximum-subarray/
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
import sys

class Solution(object):
  def max_subarray(self, nums):
    # Kadane's algorithm
    max_of_all_indices = nums[0]
    start_index_sum_ending_at_i = end_index_sum_ending_at_i = 0
    start_index_global_max = end_index_global_max = 0
    for i in range(1, len(nums)):
      if nums[i - 1] > 0:
        nums[i] += nums[i - 1]
      else:
        nums[i] = nums[i]
        start_index_sum_ending_at_i = i
      end_index_sum_ending_at_i = i
      if max_of_all_indices < nums[i]:
        max_of_all_indices = nums[i]
        start_index_global_max, end_index_global_max = start_index_sum_ending_at_i, end_index_sum_ending_at_i
    return max_of_all_indices, start_index_global_max, end_index_global_max

  def max_subarray_divide_and_conquer(self, nums):
    def cross_sum(nums):
      pivot = len(nums) // 2
      left_sum = -sys.maxint -1
      for i in range(pivot-1, -1, -1):
        if i == pivot-1:
          left_sum = nums[i]
          continue
        nums[i] += nums[i+1]
        left_sum = max(left_sum, nums[i])
      right_sum = -sys.maxint -1
      for i in range(pivot, len(nums)):
        if i == pivot:
          right_sum = nums[i]
          continue
        nums[i] += nums[i-1]
        right_sum = max(right_sum, nums[i])
      return left_sum + right_sum

    # Divide and Conquer
    if len(nums) == 0: return -sys.maxint - 1
    if len(nums) == 1: return nums[0]
    pivot = len(nums)//2
    left_sum = self.max_subarray_divide_and_conquer(nums[:pivot])
    right_sum = self.max_subarray_divide_and_conquer(nums[pivot:])
    cross_sum = cross_sum(nums[:])
    ret = max(left_sum, right_sum, cross_sum)
    return ret

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    # maxsum, start, end = sol.maxSubArray0(nums)
    # print((maxsum, start, end))
    # print((maxsum, nums[start], nums[end]))
    # maxsum, start, end = sol.max_subarray(nums)
    # print((maxsum, start, end))
    # print((maxsum, nums[start], nums[end]))
    # print(sol.maxSubArray1(nums))
    # print maxsum
    print(sol.max_subarray_divide_and_conquer(nums))
