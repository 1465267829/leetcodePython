"""
https://leetcode.com/problems/house-robber/

198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum amount of money
you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


F(i) is the max amount that we could get after 'considering' the ith
house. 'Considering' a house is not necessarily robbing it.

Here the idea is that at ith house, we have following choices:

1.  Rob the house at ith index, because we haven't robbed the i-1th house.
    Max amount we would have at this point after robbing ith house:
    Max till i-2th house + value of ith house
    That is:
    F(i-2) + "value of house at ith index"

2.  Don't rob the house at ith index, because we have robbed i-1th house.
    Max amount we would have at this point after robbing ith house:
    Max till i-1th house
    That is:
    F(i-1)

3.  While considering ith house we need to consider the max of option1 and
    option2 from above
    That is:
    F(i) = max(F(i-2) + nums[i], F(i-1))

Recurrent equation:
    F(i) = max(F(i-2) + nums[i], F(i-1))

Base Case:
    F(i) = nums[0] i == 0
    F(i) = max(nums[0], nums[1]) i == 1
"""

from typing import *


class Solution:
  def rob(self, nums: List[int]) -> int:
    if not nums: return 0
    memo = []
    for house in range(len(nums)):
      if house == 0:
        memo.append(nums[house])
        continue
      max_till_house_minus_1 = 0 if house-1 < 0 else memo[house-1]
      max_till_house_minus_2 = 0 if house-2 < 0 else memo[house-2]
      memo.append(max(max_till_house_minus_1, max_till_house_minus_2+nums[house]))
    return memo[-1]


if __name__ == '__main__':
  # nums = [1,2,3,1]
  # nums = [2,7,9,3,1]
  nums = [2,3,2]
  sol = Solution()
  print(sol.rob(nums))
