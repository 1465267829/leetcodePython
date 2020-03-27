"""
https://leetcode.com/problems/min-cost-climbing-stairs/

746. Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999]

Recurrence equation
min_price(i) = cost[i] + min(min_price(i-1), min_price(i-2))
Base Case:
min_price(i) = 0 if i < 0

Way to thinking,
How may way one ends up at ith stair(i.e top of floor)?
- Penultimate stair being i-1
- Penultimate stair being i-2
- If the cost to reach i-1th, and i-2th stair is min_price(i-1) and min_price(i-2) respectively
- then, in_price(i) = min(min_price(i-1),  min_price(i-2)) + cost[i]
Base cases:
Cost of any -ive stair is 0
Handled in code below as b and c

Cost of top floor itself is 0
Handled in code below as a

Above base cases are arrived at trivially
"""
from typing import *


class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    table = []
    for i in range(len(cost)+1):
      a = cost[i] if 0 <= i < len(cost) else 0
      b = 0 if i-1 < 0 else table[i-1]
      c = 0 if i-2 < 0 else table[i-2]
      table.append(a + min(b, c))
    return table[-1]


if __name__ == '__main__':
  sol = Solution()
  cost = [10, 15, 20]
  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
  print(sol.minCostClimbingStairs(cost))

