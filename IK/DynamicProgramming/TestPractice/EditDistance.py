"""
https://leetcode.com/problems/edit-distance/

72. Edit Distance

Given two words strWord1 and strWord2, find the minimum number of operations required to convert strWord1 to strWord2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: strWord1 = "horse", strWord2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: strWord1 = "intention", strWord2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
from typing import *


class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    memo = []
    for row in range(len(word1) + 1):
      temp_row = []
      for col in range(len(word2) + 1):
        temp_row_val = None
        if row == len(word1):
          temp_row_val = len(word2) - col
        if col == len(word2):
          temp_row_val = len(word1) - row
        temp_row.append(temp_row_val)
      memo.append(temp_row)

    for row in range(len(word1)-1, -1, -1):
      for col in range(len(word2)-1, -1, -1):
        if word1[row] == word2[col]:
          memo[row][col] = memo[row+1][col+1]
        else:
          memo[row][col] = 1 + min(
            memo[row][col+1],
            memo[row+1][col],
            memo[row+1][col+1]
          )
    return memo[0][0]


if __name__ == '__main__':
  sol = Solution()
  word1, word2 = 'horse', 'ros'
  print(sol.minDistance(word1, word2))