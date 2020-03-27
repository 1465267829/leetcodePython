"""
https://leetcode.com/problems/pascals-triangle-ii/

119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import *


class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    prev, curr = [], []
    for row in range(rowIndex+1):
      prev = curr
      curr = []
      if row == 0:
        curr.append(1)
        continue
      for col in range(row+1):
        a = prev[col] if prev and 0 <= col < len(prev) else 0
        b = prev[col-1] if prev and 0 <= col-1 < len(prev) else 0
        curr.append(a + b)
    return curr


if __name__ == '__main__':
  sol = Solution()
  print(sol.getRow(3))
