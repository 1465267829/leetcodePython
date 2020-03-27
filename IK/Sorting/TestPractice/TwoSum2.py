"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

from typing import *

class Solution:
  def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
    # TLE: Time limit exceeded
    for i in range(0, len(numbers)-1):
      for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target: return [i+1, j+1]
        if numbers[i] + numbers[j] > target: continue
    # We shouldn't be here
    # as, "You may assume that each input would have exactly one solution "
    return [-1, -1]

  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
      current_sum = numbers[i] + numbers[j]
      if target == current_sum:
        return [i+1, j+1]
      elif target < current_sum:
        j -= 1
        # handle duplicate elements to save time
        while i < j and numbers[j] == numbers[j+1]: j-=1
      else:
        i += 1
        # handle duplicate elements to save time
        while i < j and numbers[i] == numbers[i-1]: i+=1
    return [-1, -1]

if __name__ == '__main__':
  sol = Solution()
  numbers, target = [2, 7, 11, 15], 9



  print(sol.twoSum(numbers, target))