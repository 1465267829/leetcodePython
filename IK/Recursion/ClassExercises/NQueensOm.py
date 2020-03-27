"""
https://leetcode.com/problems/n-queens/

51. N-Queens


The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

"""
from typing import *


class Solution:
  def arrangeBoard(self, result, queens):
    chessboards = []
    for i in range(len(result)):
      chessboard = []
      for j in range(queens):
        chessboard_row = []
        for k in range(queens):
          if k == result[i][j]:
            chessboard_row.append('Q')
          else:
            chessboard_row.append('.')
        chessboard.append(''.join(chessboard_row))
      chessboards.append(chessboard)
    return chessboards

  def helper(self, queens, queens_col, slate, result):
    # back tracking
    last_queen = len(slate) - 1

    # last queen in same row as any previous queens
    # taken care of implicitly as we have assigned one queen per row

    # last queen in same col as any previous queens
    for previous_queen in range(len(slate) - 1):
      if slate[last_queen] == slate[previous_queen]:
        return

    # last queen in same diagonal as any previous queens
    for previous_queen in range(len(slate) - 1):
      # if colsdiff == rowsdiff then queens are at each others diagonals
      if abs(slate[last_queen] - slate[previous_queen]) == abs(last_queen - previous_queen):
        return

    # base
    if queens_col == queens:
      result.append(slate[:])
      return

    # recursive
    for col in range(0, queens):
      slate.append(col)
      self.helper(queens, queens_col + 1, slate, result)
      slate.pop()
    return

  def solveNQueens(self, n: int) -> List[List[str]]:
    queens, queens_col, slate, result = n, 0, [], []
    self.helper(queens, queens_col, slate, result)
    ret = self.arrangeBoard(result, queens)
    return ret


if __name__ == '__main__':
  sol = Solution()
  print(sol.solveNQueens(4))