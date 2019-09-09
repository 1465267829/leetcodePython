'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
'''
class SolutionnumIslands(object):
  def dfs(self, grid, row, column):
    num_grid_row = len(grid)
    num_grid_col = len(grid[0])

    if row < 0 or column < 0 or row >= num_grid_row or column >= num_grid_col or grid[row][column] == 0:
      return

    grid[row][column] = 0
    self.dfs(grid, row, column - 1)
    self.dfs(grid, row, column + 1)
    self.dfs(grid, row - 1, column)
    self.dfs(grid, row + 1, column)

  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not len(grid):
      return 0

    num_grid_row = len(grid)
    num_grid_col = len(grid[0])
    island_count = 0

    for grid_row in range(num_grid_row):
      for grid_col in range(num_grid_col):
        if grid[grid_row][grid_col] == 1:
          island_count += 1
          self.dfs(grid, grid_row, grid_col)
          v = 0 # for debug point

    return island_count

class SolutionnumIslandsIterative(object):
  def numIslandsIterative(self, grid):
    if grid is None or \
      len(grid) == 0 or \
      len(grid[0]) == 0:
      return 0

    island_count = 0
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 1:
          island_count +=1
        self.zero_neighbours(grid, row, col)

  def zero_neighbours(self, grid, row, col):
    queue = [(row, col)]

    while queue:
      current_row, current_col = queue.pop(0)
      neighbours = [
        (current_row - 1, current_col),
        (current_row + 1, current_col),
        (current_row, current_col - 1),
        (current_row, current_col + 1),
      ]
      for neighbour_row, neighbour_col in neighbours:
        if 0 <= neighbour_row < len(grid) and \
          0 <= neighbour_col < len(grid[0]) and \
          grid[neighbour_row][neighbour_col] == 1:
          queue.append((neighbour_row, neighbour_col))
    return

# if __name__ == '__main__':
#   grid = [
#     [1, 1, 1, 0],
#     [0, 1, 0, 1],
#     [1, 0, 0, 0],
#     [1, 0, 1, 1]
#   ]
#   s = SolutionnumIslands()
#   print(s.numIslands(grid))

if __name__ == '__main__':
  grid = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 1]
  ]
  s = SolutionnumIslands()
  print(s.numIslands(grid))