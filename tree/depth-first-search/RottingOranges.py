'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
'''
class SolutionorangesRotting(object):
  def orangesRotting(self, grid):

    fresh_count = 0
    rotten_coodinates = []
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1: fresh_count += 1
        elif grid[r][c] == 2: rotten_coodinates.append((r, c))
        pass
    pass

    if fresh_count == 0: return 0
    if len(rotten_coodinates) == 0: return -1
    epoc = 0

    while rotten_coodinates:
      for _ in range(len(rotten_coodinates)):
        rotten_row, rotten_col = rotten_coodinates.pop(0)
        neigbours = [
          (rotten_row - 1, rotten_col),
          (rotten_row + 1, rotten_col),
          (rotten_row, rotten_col - 1),
          (rotten_row, rotten_col + 1)
        ]
        for neigbour_row, neigbour_col  in neigbours:
          if (0 <= neigbour_row < len(grid)) and \
             (0 <= neigbour_col < len(grid[0])) and \
             grid[neigbour_row][neigbour_col] == 1:
            grid[neigbour_row][neigbour_col] = 2
            fresh_count -= 1
            rotten_coodinates.append((neigbour_row, neigbour_col))
      epoc += 1

    result = -1 if fresh_count else (epoc - 1)
    return result

if __name__ == '__main__':
  sol = SolutionorangesRotting()
  grid = [[2, 1, 1], [0, 1, 1], [0, 0, 1]]

  # grid = [[1,2,1,1,2,1,1]]

  print(sol.orangesRotting(grid))