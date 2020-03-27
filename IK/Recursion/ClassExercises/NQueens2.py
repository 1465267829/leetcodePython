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
  def totalNQueens(self, n: int) -> List[List[str]]:
    def is_valid_choice(current_queen_col_choice):
      for prev_queen_row, prev_queen_col in enumerate(slate):
        '''
        we iterate over each previous queens' positions and
        check if the current_queen_col_choice will be invalid
        for any of the previous queens' choice 
        '''
        if prev_queen_col == current_queen_col_choice:
          '''
          if this prev_queen_col is already in a column
          which is being proposed for current queen then it's 
          not a valid position for current queen. Backtrack.
          '''
          return False
        current_queen_row = len(slate)
        if abs(prev_queen_row - current_queen_row) == abs(prev_queen_col - current_queen_col_choice):
          '''
          if current proposed position makes the current queen in diagonal
          any of te previous queens then it's not a valid position for the
          current queen. Backtrack.
          '''
          return False
      '''
      Fact that we have not backtracked yet suggests that current_queen_col_choice
      is a valid one.
      '''
      return True

    def helper():
      if len(slate) == n:
        result[0] += 1
        return

      for current_queen_col_choice in range(n):
        '''
        for loop generates all possible choices for queen's column
        in the current row.

        is_valid_choice backtracks all the choices that make the
        current choice of position invalid.
        '''
        if is_valid_choice(current_queen_col_choice):
          slate.append(current_queen_col_choice)
          helper()
          slate.pop()

    '''
    Ideally the queen(s) on chessboard can choose to go across
    any row or any column from her starting position.

    This would lead to huge amount combinations of queens' position
    on the chessboard.
    We constraint the positions by starting with premise that each
    queen needs to be in unique row which is a valid premise.

    This leads us to create a slate as following:

    slate:
    slate is a list which represents the following
    slate's indexes represent the rows on the chessboard.
    slate's value in any index represents column in the row in which queen is positioned.
    For example:
    if slate is [3, 1, 2, 0]
    This means:
    queen #0 at 0th row is in 3rd column
    queen #1 at 1st row is in 1st column
    queen #2 at 2nd row is in 2nd column
    queen #3 at 3rd row is in 0th column

    Once the slate grows to length == n then we know that we have decided
    each queens position on the board.

    This is a combinatory problem where we need to generate all slates
    of length n where each cell of slate can have possible choices from
    [0, n-1] representing the queen's position column.

    We weed out invalid combinations as we create them by backtracking.
    '''
    slate, result = [], [0]
    helper()
    return result[0]


if __name__ == '__main__':
  sol = Solution()
  n = 4
  print(sol.totalNQueens(n))