"""
https://leetcode.com/problems/unique-paths-ii/

63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Recurrent equation is:

f(i,j) represents unique number of paths ro reach from [0,0] to [i,j]
location on the grid, if the robot is allowed to go only right or down
and starts at [0,0]

f(i,j) = 0 if grid[i][j) == 1
f(i,j) = f(i-1, j) + f(i, j-1) if grid[i][j) == 0

Base cases:
f(i,j) = 1, i=0 or j=0 and grid[i][j) == 0
f(i,j) = 0, i=0 or j=0 and grid[i][j) == 1

"""
from typing import *


class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    n, m = len(obstacleGrid), len(obstacleGrid[0])
    table = [[0] * m for _ in range(n)]
    for row in range(0, n):
      for col in range(0, m):
        # Base case 0
        if row == 0 and col == 0 and obstacleGrid[row][col] == 0:
          table[row][col] = 1
        elif row == 0 and col == 0 and obstacleGrid[row][col] == 1:
          # Base case 1
          table[row][col] = 0
        elif obstacleGrid[row][col] == 1:
          table[row][col] = 0
        else:
          a = table[row - 1][col] if 0 <= row - 1 < len(table) else 0
          b = table[row][col - 1] if 0 <= col - 1 < len(table[0]) else 0
          table[row][col] = a + b
    return table[-1][-1]


if __name__ == '__main__':
  sol = Solution()
  # grid = [
  #   [0,0,0],
  #   [0,1,0],
  #   [0,0,0]
  # ] # ans: 2
  # grid = [[1]] # ans: 0
  grid = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]] # ans: 1
  print(sol.uniquePathsWithObstacles(grid))
