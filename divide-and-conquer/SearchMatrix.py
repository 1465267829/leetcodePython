'''
https://leetcode.com/problems/search-a-2d-matrix-ii/
240. Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
https://www.youtube.com/watch?v=Ohke9-qwAKU
'''
class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or 0 == len(matrix) or 0 == len(matrix[0]): return False
    row, col = 0, len(matrix[0]) - 1
    while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
      if matrix[row][col] == target:
        return True
      elif matrix[row][col] < target:
        row += 1
      else:
        col -= 1
    return False

if __name__ == '__main__':
  sol = Solution()
  m, target = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ], 5
  print(sol.searchMatrix(m, target))