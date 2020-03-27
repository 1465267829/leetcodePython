"""
https://leetcode.com/problems/letter-case-permutation/

784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import *


class Solution:
  def helper_immutable_slate(self, s, index_s, slate, result):
    # immutable slate
    if index_s == len(s):
      result.append(slate)
      return

    if s[index_s].isalpha():
      self.helper(s, index_s + 1, slate + s[index_s].lower(), result)
      self.helper(s, index_s + 1, slate + s[index_s].upper(), result)
    else:
      self.helper(s, index_s + 1, slate + s[index_s], result)
    return

  def letterCasePermutationUsingImmutableSlate(self, S: str) -> List[str]:
    result = []
    self.helper(S, 0, '', result)
    return result

  def helper(self, s, index_s, slate, result):
    # mutable slate
    if index_s == len(s):
      # creates a string out of mutable slate/char array
      result.append(''.join(slate))
      return

    if s[index_s].isalpha():
      slate.append(s[index_s].lower())
      self.helper(s, index_s + 1, slate, result)
      slate.pop()

      slate.append(s[index_s].upper())
      self.helper(s, index_s + 1, slate, result)
      slate.pop()
    else:
      # isdigit(): True
      slate.append(s[index_s])
      self.helper(s, index_s + 1, slate, result)
      slate.pop()
    return

  def letterCasePermutation(self, S: str) -> List[str]:
    result, slate = [], []
    self.helper(S, 0, slate, result)
    return result


if __name__ == '__main__':
  s = 'a1b2'
  # s = '3z4'
  # s = '12345'
  sol = Solution()
  print(sol.letterCasePermutation(s))
