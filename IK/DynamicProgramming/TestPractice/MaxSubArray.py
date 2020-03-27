"""
https://leetcode.com/problems/maximum-subarray/

53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

Way of thinking:
Let F(i) be the function which, for a given list; gets us
the maximum sum of subarray ending at index i

1.  Suppose we know that the maximum subarray sum for a subarray
    ending at i-1th index. i.e we know the vale of F(i-1)

    Our choices for a subarray ending at ith index are:
    a.  Extend the subarray ending at i-1th index to include current index i.
        If we do so, the subarray sum ending at ith index becomes
        F(i-1) + "value of element at index i"
    b.  We don't extend the array ending at i-1th index. It means we start a new
        array at ith index. If we do so, the subarray sum ending at ith index becomes
        "value of element at index i". Such a subarray has only one element, the
        element at ith index.

    For index i, we decide the max of the above choices.

2.  Maximum sum subarray ending at index 0 has be an array with just one element,
    the element at 0th location. Sum of such a subarray is the 0th element itself.

3.  We perform the steps mentioned in Step1 for every index after 0th index. To find
    what is the maximum sum of a subarray ending at index i.

4.  Once we know maximum sum for subarrays ending at each index. The answer is the max among
    all of the maxes.

Recurrent equation:
F(i) = Max over j from 0..len(nums) [Max( F(i-1) + nums[i], nums[i])]
Base case:
F(i) = nums[i] i == 0

Answer :
"""

from typing import *


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    table = [0] * len(nums)
    table[0] = nums[0]

    for i in range(1, len(nums)):
      table[i] = max(table[i-1] + nums[i], nums[i])
    return max(table)


if __name__ == '__main__':
  sol = Solution()
  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  # nums = [-1,0,-2]
  print(sol.maxSubArray(nums))