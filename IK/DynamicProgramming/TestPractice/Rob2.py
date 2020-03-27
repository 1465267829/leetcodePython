"""
https://leetcode.com/problems/house-robber-ii/

213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

This problem differs from "198. House Robber [https://leetcode.com/problems/house-robber/]"
in that here houses are arranged in a circle

Here we need to consider breaking the circle and deal with houses at the broken
edge separately. Once we break the circle and deal with edge case arouns the broken edge,
we should be able to deal with the rest of houses as if they are in a line just like
"198. House Robber".

Let's say houses are numbered as per the indices of given nums
i.e 0..n-1. We decide to break the circle between 0 and n-1. After breaking the
circle we have following cases that emerge:

1.  Case 1: Rob 0th house
    In this case we decide to rob 0th house, then house 1th and n-1th are out
    of consideration list.
    The consideration list becomes 2..n-2th house. Considered list can be treated as
    a row of houses just like "198. House Robber".

    Once we find the maximum amount for considered houses from 2..n-2, we add 0th house's value to
    the amount to get the maximum amount we get after robbing 0th house and subsequent
    houses as per rules

2.  Case 2: Don't rob 0th house
    In this case we decide to skip robbing 0th house, then house 1..n-1 are for robbing
    as if they were in a row just like "198. House Robber".

    We find the the maximum amount for considered houses 1..n-1.

3. Max of Case 1 and Case 2 is the answer

"""

from typing import *


class Solution:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return 0
    if n == 1:
      return nums[0]
    if n == 2:
      return max(nums[0], nums[1])
    if n == 3:
      return max(nums[0], nums[1], nums[2])
    if n == 4:
      return max(nums[0] + nums[2], nums[1] + nums[3])

    # Case 1: Rob house 0
    table = [0] * n
    table[0] = 0  # Pretend we didn't rob house 0, we will add it later
    table[1] = 0  # house 0 robbed, can't rob house 1
    table[2] = nums[2] # here onwards treat the houses like single line till n-2th house
    table[3] = max(nums[2], nums[3])
    for i in range(4, n-1):
      table[i] = max(nums[i]+table[i-2], table[i-1])
    case_1 = table[n-2] + nums[0] # add value of 0th house to max

    # Case 2: Don't rob house 0
    table[0] = 0 # we don't rob house 0
    table[1] = nums[1] # here onwards treat houses like single line till n-1th house
    table[2] = max(nums[1], nums[2])
    for i in range(3, n):
      table[i] = max(nums[i] + table[i - 2], table[i - 1])
    case_2 = table[n-1]
    return max(case_1, case_2)


if __name__ == '__main__':
  sol = Solution()
  nums = [2,3,2]
  print(sol.rob(nums))