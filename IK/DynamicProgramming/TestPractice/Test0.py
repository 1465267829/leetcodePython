def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
  n, m = len(obstacleGrid), len(obstacleGrid[0])
  table = [[0] * m for _ in range(n)]
  for row in range(0, n):
    for col in range(0, m):
      # Base case 0
      if row == 0 and col == 0 and obstacleGrid[row][col] == 0:
        table[row][col] = 1
      elif row == 0 and col == 0 and obstacleGrid[row][col] == 1:
        # Base case 1
        table[row][col] = 0
      elif obstacleGrid[row][col] == 1:
        table[row][col] = 0
      else:
        a = table[row - 1][col] if 0 <= row - 1 < len(table) else 0
        b = table[row][col - 1] if 0 <= col - 1 < len(table[0]) else 0
        table[row][col] = a + b
  return table[-1][-1]

def numberOfPaths(matrix):
  n, m = len(matrix), len(matrix[0])
  table = [[0] * m for _ in range(n)]
  for row in range(0, n):
    for col in range(0, m):
      # Base case 0
      if row == 0 and col == 0 and matrix[row][col] == 1:
        table[row][col] = 1
      elif row == 0 and col == 0 and matrix[row][col] == 0:
        # Base case 1
        table[row][col] = 0
      elif matrix[row][col] == 0:
        table[row][col] = 0
      else:
        a = table[row - 1][col] if 0 <= row - 1 < len(table) else 0
        b = table[row][col - 1] if 0 <= col - 1 < len(table[0]) else 0
        table[row][col] = a + b
  return table[-1][-1]