"""
https://leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

https://www.youtube.com/watch?v=kT_VabdscHk
"""

from typing import *


class Solution:
  '''
  Recurrance equation:
  C(n) = 1 for n = 0
  C(n) = 1 for n = 1
  C(n) = Sum Over i where i is between 1 to n C(i-1)*C(n-i)
  i.e C(3) = C(1-1)*C(3-1) + C(2-1)*C(3-2) + C(3-1)*C(3-3)

  '''
  def numTrees(self, n: int) -> int:
    if n == 0: return 0
    memo = [1, 1]
    for n in range(2, n + 1):
      value = 0
      for i in range(1, n + 1):
        value += memo[i - 1] * memo[n - i]
      memo.append(value)
    return memo[n]


if __name__ == '__main__':
  sol = Solution()
  print(sol.numTrees(5))