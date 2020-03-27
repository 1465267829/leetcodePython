"""

https://leetcode.com/problems/triangle/

120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Way to think:
This is like minimum path sum problem with the following differences:
1.  The grid is given in a triangle format.
    The generated grid from the triangle is left aligned.
2.  Unoccupied nodes in grid are init'd at INF
3.  The answer is the minimum of last row of memo table

Recurrent equation is:

If F(i,j) represents the minimum path sum of a path of all the paths
that originate at [0, 0] and end at [i,j] of the given triangle 2D array.

Then

F(i,j) = grid[i,j] + min( F(i-1, j), F(i-1, j-1)) for any i and j in bounds of the grid/triangle

Base Case:
F(i, j) = INF if i or j are out of bounds of the grid/triangle.

"""

from typing import *
from math import inf


class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    table = [[inf] * len(triangle[-1]) for _ in range(len(triangle))]

    for row in range(len(table)):
      for col in range(len(triangle[row])):
        if row == 0 and col == 0:
          table[row][col] = triangle[0][0]
        else:
          a = table[row-1][col] if 0 <= row-1 < len(table) and 0 <= col < len(table[0]) else inf
          b = table[row-1][col-1] if 0 <= row-1 < len(table) and 0 <= col-1 < len(table[0]) else inf
          table[row][col] = triangle[row][col] + min(a, b)
    return min(table[-1])


if __name__ == '__main__':
  sol = Solution()
  triangle = [
       [2],
      [3,4],
     [6,5,7],
    [4,1,8,3]
  ]
  print(sol.minimumTotal(triangle))