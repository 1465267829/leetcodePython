"""
https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import *


class Solution:
  def helper(self, num_left, num_right, slate, result):
    # backtracking case
    if num_left < 0 or num_right < 0 or num_left > num_right:
      # if we ran out of left or right parenthesis then we clearly
      # won't have any legal combination anymore
      # OR
      # or if number of left parenthesis are more than
      # number of right parenthesis, then we clearly won't have any legal
      # permutation anymore
      return

    # base case:
    if num_left == 0 and num_right == 0:
      result.append(''.join(slate))
      return

    # recursive case
    slate.append('(')
    self.helper(num_left-1, num_right, slate, result)
    slate.pop()

    slate.append(')')
    self.helper(num_left, num_right-1, slate, result)
    slate.pop()
    return

  def generateParenthesis(self, n: int) -> List[str]:
    num_left, num_right, slate, result = n, n, [], []
    self.helper(num_left, num_right, slate, result)
    return result


if __name__ == '__main__':
  sol = Solution()
  print(sol.generateParenthesis(3))