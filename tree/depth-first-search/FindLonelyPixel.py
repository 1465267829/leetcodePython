'''
531. Lonely Pixel I
https://leetcode.com/problems/lonely-pixel-i/
'''

class Solution(object):
  def findLonelyPixel(self, picture):
    """
    :type picture: List[List[str]]
    :rtype: int
    """
    if not len(picture) or not len(picture): return 0

    num_rows = len(picture)
    num_cols = len(picture[0])
    track_rows = num_rows * [0]
    track_cols = num_cols * [0]

    for i in range(num_rows):
      for j in range(num_cols):
        if picture[i][j] == 'B':
          track_rows[i] += 1
          track_cols[j] += 1

    black_lonely = 0
    for i in range(num_rows):
      for j in range(num_cols):
        if picture[i][j] == 'B' and track_rows[i] == 1 and track_cols[j] == 1:
          black_lonely += 1
    return black_lonely

if __name__ == '__main__':
  picture  = [["W","W","B"],["W","B","W"],["B","W","W"]]
  picture  = [["B","B","W","B","W","B","B","B","B","W"],["W","B","W","B","B","W","W","W","W","B"],["W","B","B","B","W","W","B","W","W","B"],["W","W","W","W","W","W","W","B","W","W"],["W","B","B","W","W","W","B","B","W","B"],["B","B","B","B","W","B","W","B","W","B"],["W","W","B","B","B","W","B","W","W","B"],["B","W","W","B","B","W","W","W","W","W"],["B","W","B","W","W","B","W","B","B","W"],["B","B","B","B","W","W","W","B","B","W"]]
  sol = Solution()
  print(sol.findLonelyPixel(picture))