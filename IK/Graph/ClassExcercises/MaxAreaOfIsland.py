"""
https://leetcode.com/problems/max-area-of-island/

695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing import *


class Solution:
  def __init__(self):
    self.adj_matrix = None
    self.max_area_island = 0
    self.area_island = 0

  def build_graph(self, grid):
    self.adj_matrix = grid

  def dfs(self, row, col):
    self.adj_matrix[row][col] = 0
    self.area_island += 1
    neighbors = [[row+1, col], [row-1, col], [row, col + 1], [row, col-1]]
    for neighbor_row, neighbor_col in neighbors:
      if 0 <= neighbor_row < len(self.adj_matrix) and 0 <= neighbor_col < len(self.adj_matrix[0]) and self.adj_matrix[neighbor_row][neighbor_col] == 1:
        self.dfs(neighbor_row, neighbor_col)

  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    self.build_graph(grid)
    for row in range(len(self.adj_matrix)):
      for col in range(len(self.adj_matrix[0])):
        if self.adj_matrix[row][col] == 1:
          self.area_island = 0
          self.dfs(row, col)
          self.max_area_island = max(self.max_area_island, self.area_island)
    return self.max_area_island


if __name__ == '__main__':
  sol = Solution()
  grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
  ]
  # grid = [[0,0,0,0,0,0,0,0]]
  print(sol.maxAreaOfIsland(grid))

