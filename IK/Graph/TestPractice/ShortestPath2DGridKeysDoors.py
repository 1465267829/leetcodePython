# def find_shortest_path(grid):
#
#   def get_neighbors(row, col):
#     result = []
#     neighbors = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
#     for nrow, ncol in neighbors:
#       if 0 <= nrow < len(grid):
#         # if the nrow is in range
#         continue
#       if 0 <= ncol < len(grid[0]):
#         # if the nrow is in range
#         continue
#       if grid[nrow][ncol] == '#':
#         # if current neighbor cell water
#         continue
#       if visited[nrow][ncol] == 1:
#         # if current neighbor cell is already visited
#         continue
#       neighbor = grid[nrow][nrow]
#       if neighbors == '+':
#         # if current neighbor cell is goal, add it
#         result.append([nrow, nrow])
#         continue
#       if neighbor.isalpha() and neighbor.islower():
#         # if current neighbor cell is key
#         # add the key to keys
#         keys[neighbor] += 1
#         result.append([nrow, nrow])
#         continue
#       if neighbor.isalpha() and neighbor.isupper():
#         # if current neighbor cell is lock
#         # check if we have keys
#         if keys[neighbor]:
#           # if we have keys, decrease the key and add the cell to legitimate neighbor
#           keys[neighbor] -= 1
#           result.append([nrow, nrow])
#         continue
#     return result
#
#   def dfs(row, col):
#     stack.append([[row, col]])
#     current_cell = grid[row][col]
#
#     if current_cell == '+':
#       # found the destination
#       pass
#     for n_row, n_col in get_neighbors(row, col):
#       visited[row][col] = 1
#       dfs(n_row, n_col)
#
#     # # if current element is key, return the unused key
#     # if current_cell.isalpha() and current_cell.islower():
#     #   keys[current_cell] -= 1
#
#     # pop ourselves
#     stack.pop()
#
#
#   visited = [[0] * len(grid[0]) for _ in len(grid)]
#   start_row, start_col = None, None
#   end_row, end_col = None, None
#   keys = {}
#   stack = []
#   for i in range(26):
#     keys.setdefault(chr(ord('a') + i), 0)
#
#
#
#   for row in range(len(grid)):
#     for col in range(len(grid[0])):
#       if grid[row][col] == '@':
#         start_row, start_col = row, col
#       if grid[row][col] == '+':
#         end_row, end_col = row, col
#
#   dfs(start_row, start_col)

