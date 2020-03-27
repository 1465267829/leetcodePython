"""
https://leetcode.com/problems/fibonacci-number/

509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(phonenumberlength) = F(phonenumberlength - 1) + F(phonenumberlength - 2), for phonenumberlength > 1.
Given phonenumberlength, calculate F(phonenumberlength).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

from typing import *


class Solution:
  """
  recurrence equation:
  F(0) = 0,   F(1) = 1
  F(phonenumberlength) = F(phonenumberlength - 1) + F(phonenumberlength - 2), for phonenumberlength > 1.
  Optimised memo by mod method
  """
  def fib(self, N: int) -> int:
    # here we take a bottom's up approach
    # coding the recurrence equation directly
    # optimizing for memo stack as Omkar suggested
    memo = [0, 1, -1]
    for i in range(2, N+1):
      index = i % 3
      memo[index] = sum(memo) - memo[index]
    index = N % 3
    return memo[index]


if __name__ == '__main__':
  sol = Solution()
  print(sol.fib(20000))
