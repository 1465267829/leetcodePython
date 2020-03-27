"""
https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import *


class Solution:
  def __init__(self):
    self.adj_matrix = None

  def build_graph(self, grid):
    self.adj_matrix = grid

  def dfs(self, row, col):
    self.adj_matrix[row][col] = '0'
    neighbors = [[row, col+1], [row+1, col], [row, col-1], [row-1, col]]
    for neighbor_row, neighbor_col in neighbors:
      if 0 <= neighbor_row < len(self.adj_matrix) and 0 <= neighbor_col < len(self.adj_matrix[0]) and self.adj_matrix[neighbor_row][neighbor_col] == '1':
          self.dfs(neighbor_row, neighbor_col)

  def numIslands(self, grid: List[List[str]]) -> int:
    self.build_graph(grid)
    count = 0
    for row in range(len(self.adj_matrix)):
      for col in range(len(self.adj_matrix[0])):
        if self.adj_matrix[row][col] == '1':
          count += 1
          self.dfs(row, col)
    return count


if __name__ == '__main__':
  sol = Solution()
  # grid = [
  #   [1, 1, 1, 0],
  #   [0, 1, 0, 1],
  #   [1, 0, 0, 0],
  #   [1, 0, 1, 1]
  # ]
  grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
  ]
  print(sol.numIslands(grid))
  pass
