"""
https://leetcode.com/problems/flood-fill/

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""
from typing import *


class Solution:
  def __init__(self):
    self.adj_matrix = None
    self.newColor = None
    self.oldColor = None

  def build_graph(self, grid):
    self.adj_matrix = grid

  def dfs(self, row, col):
    self.adj_matrix[row][col] = self.newColor
    neighbors = [[row, col+1], [row+1, col], [row, col-1], [row-1, col]]
    for neighbor_row, neighbor_col in neighbors:
      if 0 <= neighbor_row < len(self.adj_matrix) and 0 <= neighbor_col < len(self.adj_matrix[0]) and self.adj_matrix[neighbor_row][neighbor_col] == self.oldColor:
          self.dfs(neighbor_row, neighbor_col)

  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    self.build_graph(image)
    self.newColor = newColor
    self.oldColor = self.adj_matrix[sr][sc]
    if self.oldColor != self.newColor:
      self.dfs(sr, sc)
    return self.adj_matrix


if __name__ == '__main__':
  sol = Solution()
  # image, sr, sc, newColor = [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2
  image, sr, sc, newColor = [[0,0,0],[0,1,1]], 1, 1, 1
  print(sol.floodFill(image, sr, sc, newColor))