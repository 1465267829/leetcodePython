"""
https://leetcode.com/problems/minimum-path-sum/

64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Recurrent equation:
F(i, j) is the function which gives the value of
minimum sum path while travelling the grid from location [0,0] to [-1,-1]

F(i, j) = grid[i, j] + min(F(i, j-1), F(i-1, j))

Base Cases:
F(i, j) = grid[i, j] if i==0 and j==0
F(i, j) = grid[i, j] + F(i, j-1) if i==0
F(i, j) = grid[i, j] + F(i-1, j) if j==0
"""

from typing import *


class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    table = [[0] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(table)):
      for col in range(len(table[0])):
        if row == 0 and col == 0:
          table[row][col] = grid[row][col]
        elif row == 0:
          table[row][col] = table[row][col-1] + grid[row][col]
        elif col == 0:
          table[row][col] = table[row-1][col] + grid[row][col]
        else:
          a = table[row][col-1] if 0 <= col-1 < len(table[0]) else 0
          b = table[row-1][col] if 0 <= row-1 < len(table) else 0
          table[row][col] = grid[row][col] + min(a, b)
    return table[-1][-1]


if __name__ == '__main__':
  sol = Solution()
  grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
  print(sol.minPathSum(grid))

