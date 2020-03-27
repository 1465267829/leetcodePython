"""
https://leetcode.com/problems/coin-change/

322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

from typing import *
from math import inf as inf


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    memo = [inf] * (amount+1)
    memo[0] = 0
    for index in range(1, len(memo)):
      for coin in coins:
        if index-coin >= 0:
          memo[index] = min(memo[index], memo[index-coin]+1)
    ret = memo[-1] if memo[-1] != inf else -1
    return ret


if __name__ == '__main__':
  sol = Solution()
  # coins, amount = [1, 2, 5], 11
  # coins, amount = [1, 2, 5], 2
  coins, amount = [2], 3
  print(sol.coinChange(coins, amount))
