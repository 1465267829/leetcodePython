"""
https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import *


class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for row in range(numRows):
      if row == 0:
        result.append([1])
        continue
      row_list = []
      for col in range(row+1):
        a = result[row-1][col] if 0 <= row-1 < len(result) and 0 <= col < len(result[row-1]) else 0
        b = result[row-1][col-1] if 0 <= row-1 < len(result) and 0 <= col-1 < len(result[row-1]) else 0
        row_list.append(a + b)
      result.append(row_list)
    return result


if __name__ == '__main__':
  sol = Solution()
  print(sol.generate(5))
