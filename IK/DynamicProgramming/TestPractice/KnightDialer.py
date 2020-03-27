"""
https://leetcode.com/problems/knight-dialer/

935. Knight Dialer

A chess knight can move as indicated in the chess diagram below:

 .



This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes phonenumberlength-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing phonenumberlength digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.



Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46


Note:

1 <= phonenumberlength <= 5000
"""

from typing import *


class Solution:
  def knightDialer(self, N: int) -> int:
    MOD = 10 ** 9 + 7
    neighbors = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    memo = []
    for num_len in range(0, N + 1):
      row = []
      for digit in range(0, 10):
        if num_len == 0:
          row.append(0)
        elif num_len == 1:
          row.append(1)
        elif num_len == 2:
          row.append(len(neighbors[digit]))
        else:
          res = 0
          for neighbor_digit in neighbors[digit]:
            res += memo[num_len-1][neighbor_digit]
          row.append(res)
      memo.append(row)
    return sum(memo[len(memo)-1]) % MOD


def numPhoneNumbers(startdigit, phonenumberlength):
  neighbors = {
      0: [4, 6],
      1: [6, 8],
      2: [7, 9],
      3: [4, 8],
      4: [3, 9, 0],
      5: [],
      6: [1, 7, 0],
      7: [2, 6],
      8: [1, 3],
      9: [2, 4],
  }
  memo = []
  for num_len in range(0, phonenumberlength + 1):
    row = []
    for digit in range(0, 10):
      if num_len == 0:
        row.append(0)
      elif num_len == 1:
        row.append(1)
      elif num_len == 2:
        row.append(len(neighbors[digit]))
      else:
        res = 0
        for neighbor_digit in neighbors[digit]:
          res += memo[num_len-1][neighbor_digit]
        row.append(res)
    memo.append(row)
  return memo[phonenumberlength][startdigit]


if __name__ == '__main__':
  sol = Solution()
  # print(sol.knightDialer(3))
  print(numPhoneNumbers(1, 3))




