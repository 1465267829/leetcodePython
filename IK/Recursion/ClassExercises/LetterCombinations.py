"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from typing import *


class Solution:
  def helper(self, digits, index, phone, slate, result):
    if index == len(digits):
      result.append(''.join(slate))
      return

    for value in phone[digits[index]]:
      slate.append(value)
      self.helper(digits, index+1, phone, slate, result)
      slate.pop()

  def letterCombinations(self, digits: str) -> List[str]:
    if len(digits) == 0: return []
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    index, slate, result = 0, [], []
    self.helper(digits, index, phone, slate, result)
    return result


if __name__ == '__main__':
  digits = '23'
  sol = Solution()
  print(sol.letterCombinations(digits))


