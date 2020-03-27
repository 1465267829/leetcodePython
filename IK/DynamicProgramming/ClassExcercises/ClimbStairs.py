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


class Solution:
  def climbStairs(self, n: int) -> int:
    """
    Recurrence equation
    distinct_ways(n) = distinct_ways(n-1) + distinct_ways(n-2)
    distinct_ways(2) = 2
    distinct_ways(1) = 1

    Way to thinking,
    How may way one ends up at nth stair?
    - Penultimate stair being n-1
    - Penultimate stair being n-2
    - So, # distinct ways to reach nth stair = # of distinct ways to reach n-1th stair + # of distinct ways to reach n-2th stair
    - using https://en.wikipedia.org/wiki/Rule_of_sum
    Base case:
    Ways to reach 1st stair == 1
    Ways to reach 2nd stair == 2
    Above base cases are arrived at trivially
    """
    memo = [1, 2]
    for i in range(2, n):
      memo.append(memo[i-1] + memo[i-2])
    return memo[n-1]


if __name__ == '__main__':
  sol = Solution()
  print(sol.climbStairs(1))