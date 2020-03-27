from typing import *


class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    def zerocircle(row, col):
      M[row][col] = 0
      neighbors = list(
        filter(lambda x: 0 <= x[0] < len(M) and 0 <= x[1] < len(M[0]) and M[x[0]][x[1]] == 1,
               [[row + 1, col], [row + 1, col], [row, col + 1], [row, col - 1]])
      )
      for neighbor in neighbors: zerocircle(neighbor[0], neighbor[1])

    if not M: return 0
    circles = 0
    for row in range(len(M)):
      for col in range(len(M[0])):
        if M[row][col] == 1:
          circles += 1
          zerocircle(row, col)
    return circles


if __name__ == '__main__':
  sol = Solution()
  M = [[1,0,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,1,1]]
  print(sol.findCircleNum(M))