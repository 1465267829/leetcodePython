"""
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
from typing import *

# Brute Force
# class Solution:
#   def helper(self, n, slate, result):
#     if n == 0:
#       result.append(slate[:])
#       return
#
#     if n < 0:
#       return
#
#     # choose 1 step
#     slate.append(1)
#     self.helper(n - 1,slate, result)
#     slate.pop()
#     slate.append(2)
#     self.helper(n - 2,slate, result)
#     slate.pop()
#
#   def climbStairs(self, n: int) -> int:
#     result, slate = [], []
#     self.helper(n, slate, result)
#     return result


class Solution:

  def climbStairs(self, n: int) -> int:

    def helper(n, memo, step_sizes):
      if n == 0:
        return 1
      if n < 0: return 0

      result = 0
      for step_size in step_sizes:
        if n-step_size not in memo:
          memo[n-step_size] = helper(n-step_size, memo, step_sizes)
        result += memo[n-step_size]
      return result

    memo = {}
    step_sizes = [1, 2]
    ret = helper(n, memo, step_sizes)
    return ret


if __name__ == '__main__':
  sol = Solution()
  print(sol.climbStairs(35))
