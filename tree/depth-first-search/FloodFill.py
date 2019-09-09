'''
733. Flood Fill
https://leetcode.com/problems/flood-fill/description/
'''
class SolutionfloodFill(object):
  def floodFill(self, image, sr, sc, newColor):
    if not image or \
      not (1 <= len(image) <= 50) or \
      not (1 <= len(image[0]) <= 50) or \
      not (0 <= newColor <= 65535):
      return []

    current_color = image[sr][sc]
    # if the color to be filled is already present then return image
    if current_color == newColor: return image

    queue = [(sr, sc)]
    while queue:
      current_row, current_col = queue.pop(0)
      image[current_row][current_col] = newColor

      neighbours = [
        (current_row - 1, current_col),
        (current_row + 1, current_col),
        (current_row, current_col - 1),
        (current_row, current_col + 1),
      ]

      for neighbour_row, neighbour_col in neighbours:
        if 0 <= neighbour_row < len(image) and \
           0 <= neighbour_col < len(image[0]) and \
           image[neighbour_row][neighbour_col] == current_color:
          queue.append((neighbour_row, neighbour_col))
    return image

if __name__ == '__main__':
  sol = SolutionfloodFill()
  # print(sol.floodFill(
  #   [
  #     [1, 1, 1],
  #     [1, 1, 0],
  #     [1, 0, 1]
  #   ],
  #   1, 1, 2
  #   ))

  print(sol.floodFill(
    [[0, 0, 0], [0, 1, 1]],
    1, 1, 1
    ))
