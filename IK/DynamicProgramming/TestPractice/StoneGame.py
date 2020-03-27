"""
https://leetcode.com/problems/stone-game/

877. Stone Game

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

from typing import *


class Solution:
  def stoneGame(self, piles: List[int]) -> bool:
    coins = piles
    lenv = len(coins)
    memo = [[0] * (lenv) for i in range(lenv)]

    for i in range(lenv, -1, -1):
      for j in range(i, lenv):
        if j == i:
          memo[i][j] = coins[i]
        elif j == i + 1:
          memo[i][j] = max(coins[i], coins[j])
        else:
          a = memo[i + 2][j] if 0 <= i + 2 < lenv and 0 <= j < lenv else 0
          b = memo[i + 1][j - 1] if 0 <= i + 1 < lenv and 0 <= j - 1 < lenv else 0
          c = memo[i][j - 2] if 0 <= i < lenv and 0 <= j - 2 < lenv else 0
          # a = memo[i+2][j]
          # b = memo[i+1][j-1]
          # c = memo[i][j-2]
          # print(a, b, c)
          memo[i][j] = max(
            (coins[i] + min(a, b)),
            (coins[j] + min(b, c))
          )
    return memo[0][lenv - 1]


if __name__ == '__main__':
  sol = Solution()
  piles = [5,3,4,5]
  print(sol.stoneGame(piles))