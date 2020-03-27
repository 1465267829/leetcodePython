"""
https://leetcode.com/problems/the-maze/

490. The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

from typing import *
from queue import Queue as q


class Solution:

  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    queue = q()
    queue.put(start)
    # right, down, left, up
    children = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while not queue.empty():
      row, col = queue.get()

      if row == destination[0] and col == destination[1]:
        return True

      for dir_row, dir_col in children:
        child_row = row + dir_row
        child_col = col + dir_col
        while 0 <= child_row < len(maze) and 0 <= child_col < len(maze[0]) and maze[child_row][child_col] != 1:
          child_row += dir_row
          child_col += dir_col
        child_row -= dir_row
        child_col -= dir_col
        if maze[child_row][child_col] == 0:
          queue.put([child_row, child_col])
    return False


if __name__ == '__main__':
   sol = Solution()
   # maze = [
   #    [0, 0, 1, 0, 0],
   #    [0, 0, 0, 0, 0],
   #    [0, 0, 0, 1, 0],
   #    [1, 1, 0, 1, 1],
   #    [0, 0, 0, 0, 0],
   #  ]
   # start, destination = [0, 4], [4, 4]
   maze = [
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]
    ]
   # start, destination = [0, 4], [3, 2]
   start, destination = [0, 4], [1, 2]
   print(sol.hasPath(maze, start, destination))
