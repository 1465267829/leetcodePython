class DFS2dMatrix:
  def __init__(self):
    self.target = None

  def outofbounds(self, matrix, row, col):
    if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])):
      return True
    return False

  def dfs_helper(self, matrix, row, col, stack):
    if self.outofbounds(matrix, row, col):
      return
    # if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])):
    #   return

    if matrix[row][col] is None:
      return

    if matrix[row][col] == self.target:
      # matrix[row][col] = None
      print(stack + [matrix[row][col]])
      return

    stack.append(matrix[row][col])
    # print(matrix[row][col])
    matrix[row][col] = None
    # go right
    self.dfs_helper(matrix, row, col + 1, stack)
    # go down
    self.dfs_helper(matrix, row + 1, col, stack)
    # go left
    self.dfs_helper(matrix, row, col - 1, stack)
    # go up
    self.dfs_helper(matrix, row - 1, col, stack)
    stack.pop()

  def dfs(self, matrix, target):
    stack = []
    self.target = target
    return self.dfs_helper(matrix, 0, 0, stack)

  def bfs(self, matrix, target):
    self.target = target
    queue = [(0, 0)]
    children = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while queue:
      for _ in range(len(queue)):
        (row, col) = queue.pop(0)
        if matrix[row][col] is None:
          continue

        print(matrix[row][col])
        matrix[row][col] = None

        for child_row, child_col in children:
          child_row, child_col = child_row + row, child_col + col
          if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix[0]):
            queue.append((child_row, child_col))
      pass
    pass


if __name__ == '__main__':
  # matrix = [
  #   [0, 1, 2],
  #   [3, 4, 5],
  #   [6, 7, 8],
  # ]
  matrix = [
    [0, 1, 2, 10],
    [3, 4, 5, 20],
    [6, 7, 8, 30],
    [40, 50, 60, 70],
  ]
  sol = DFS2dMatrix()
  # sol.dfs(matrix, 4)
  sol.bfs(matrix, 4)
