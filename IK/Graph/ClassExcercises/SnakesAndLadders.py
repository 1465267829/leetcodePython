"""
https://leetcode.com/problems/snakes-and-ladders/

909. Snakes and Ladders

On an phonenumberlength x phonenumberlength board, the numbers from 1 to phonenumberlength*phonenumberlength are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= phonenumberlength*phonenumberlength.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square phonenumberlength*phonenumberlength.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the phonenumberlength*phonenumberlength-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and phonenumberlength*phonenumberlength or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number phonenumberlength*phonenumberlength has no snake or ladder.
"""

from typing import *
from math import pow


class Solution:
  def __init__(self):
    self.adj_map = {}
    self.visited = {}
    self.board = None

  def get_cooridinates(self, count):
    # given a number on board return the borad
    # coordinates
    N = len(self.board)
    quot, rem = divmod(count-1, N)
    row = N - 1 - quot
    col = rem if row % 2 != N % 2 else N - 1 - rem
    return row, col

  def build_graph(self, board):
    N = len(self.board)
    for vertex in range(1, int(pow(len(board), 2)) + 1):
      self.adj_map.setdefault(vertex, [])
      for dice in range(1, 7):
        next_move = vertex + dice
        if 1 <= next_move <= N*N:
          row, col = self.get_cooridinates(next_move)
          if self.board[row][col] != -1:
            next_move = self.board[row][col]
          self.adj_map[vertex].append(next_move)

  def bfs(self, board_display):
    queue = [board_display]
    throw_count = 0
    self.visited[board_display] = [None, throw_count]
    while queue:
      throw_count += 1
      for _ in range(len(queue)):
        current_board_display = queue.pop(0)
        for neighbor_board_display in self.adj_map[current_board_display]:
          if neighbor_board_display not in self.visited:
            self.visited[neighbor_board_display] = [current_board_display, throw_count]
            queue.append(neighbor_board_display)

  def snakesAndLadders(self, board: List[List[int]]) -> int:
    self.board = board
    self.build_graph(board)
    self.bfs(1)
    N = len(self.board)
    end = N * N
    if end not in self.visited:
      return -1
    _, throws = self.visited[end]
    return throws


if __name__ == '__main__':
  sol = Solution()
  # board = [
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,35,-1,-1,13,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,15,-1,-1,-1,-1]
  # ]
  board = [
    [1,1,-1],
    [1,1,1],
    [-1,1,1]
  ]
  print(sol.snakesAndLadders(board))