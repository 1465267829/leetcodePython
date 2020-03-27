"""
https://leetcode.com/problems/unique-paths/

62. Unique Paths
Medium

2123

156

Favorite

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

Recurrent equation is:

f(i,j) represents unique number of paths ro reach from [0,0] to [i,j]
location on the grid, if the robot is allowed to go only right or down
and starts at [0,0]

f(i,j) = f(i-1, j) + f(i, j-1)

Base cases:
f(i,j) = 1, i=0 or j=0
"""


class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    table = [[1] * m for _ in range(n)]
    for row in range(1, n):
      for col in range(1, m):
        table[row][col] = table[row-1][col] + table[row][col-1]
    return table[-1][-1]


if __name__ == '__main__':
  sol = Solution()
  # m, n = 3, 2
  m, n = 7, 3
  print(sol.uniquePaths(m, n))