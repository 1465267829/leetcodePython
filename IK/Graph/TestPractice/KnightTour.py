def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
  def get_neighbors(row, col):
    result = []
    neighbors = [
      [row-2, col-1],
      [row-2, col+1],
      [row-1, col-2],
      [row-1, col+2],
      [row+1, col-2],
      [row+1, col+2],
      [row+2, col-1],
      [row+2, col+1],
    ]
    for n_row, n_col in neighbors:
      if 0 <= n_row < rows and 0 <= n_col < cols and board[n_row][n_col] != 1:
        result.append([n_row, n_col])
    return result

  board = [[0] * cols for _ in range(rows)]
  moves = 0
  queue = [[start_row, start_col]]
  board[start_row][start_col] = 1

  while queue:
    for _ in range(len(queue)):
      cur_row, cur_col = queue.pop(0)
      if cur_row == end_row and cur_col == end_col:
        return moves
      for n_row, n_col in get_neighbors(cur_row, cur_col):
        if board[n_row][n_col] != 1:
          board[n_row][n_col] = 1
          queue.append([n_row, n_col])
    moves += 1
  return -1


if __name__ == '__main__':
  rows, cols, start_row, start_col, end_row, end_col = 5, 5, 0, 0, 4, 1
  print(find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col))