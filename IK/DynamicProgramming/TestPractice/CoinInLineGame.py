"""
IK definition
####################################################################################
Coin Play
####################################################################################

Problem Statement:
Consider a row of n coins of values v1, . . ., vn. We play a game against an opponent by alternating turns.
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and
receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
Assume full competency by both players.

Input/Output Format For The Function:

Input Format:
You will be given an array of integers v.

Output Format:
Return an integer max, denoting the maximum possible amount of sum that you can accumulate.

Input/Output Format For The Custom Input:

Input Format:
The first line should contain an integer n, denoting no. of coins. In next n lines, ith line should contain an integer vi, denoting value of ith coin in input array v.
If n = 4 and v = [8, 15, 3, 7], then input should be:
4
8
15
3
7
Output Format:
There will be only one line, containing an integer max, denoting the maximum possible amount of sum that you can accumulate.
For input n = 4 and v = [8, 15, 3, 7], output will be:
22
Constraints:

1 <= n <= 1000
1 <= v[i] <= 10^6


Sample Test Case:
Sample Input:
v = [8, 15, 3, 7]
Sample Output:
22
Explanation:
Player 1 can start two different ways: either picking 8 or picking 7. Depending on the choice s/he makes, the end reward will be different. We want to find the maximum reward the first player can collect.
1. Player 1 start by picking coin of amount 8.

Remaining v = [15, 3, 7].

Opponent will have two choices, either pick coin of value 15 or 7.
Opponent will always pick 15 (to maximize his/her own amount).

Remaining v = [3, 7].

Player 1 will have two choices, either pick coin of value 3 or 7.
Player 1 will always pick 7 (to maximize his/her own amount).

Hence in this case, player 1 can get maximum amount 8 + 7 = 15.
(This is greedy strategy i.e. pick the highest at every step.)
2. Player 1 start by picking coin of amount 7.

Remaining v = [8, 15, 3].

Opponent will have two choices, either pick coin of value 8 or 3.
Opponent will pick 8 (to maximize his/her own amount).
(Even if he/she picks 3, then also answer will be same, because in next turn player 1 is looking for coin of value 15.)

Remaining v = [15, 3].

Player 1 will have two choices, either pick coin of value 15 or 3.
Player 1 will always pick 15 (to maximize his/her own amount).

Hence in this case, player 1 can get maximum amount 7 + 15 = 22.
Given these two strategies, we want 22 as the answer, and not 15.

####################################################################################
Alternative definition
####################################################################################
Best explanation

https://algorithms.tutorialhorizon.com/dynamic-programming-coin-in-a-line-game-problem/

https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/

Recurrent equation

F(i, j)  represents the maximum value the user can collect from
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ),
                   Vj + min(F(i+1, j-1), F(i, j-2) ))
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1


####################################################################################
"""

def maxWin(coins):
  lenv = len(coins)
  memo = [[0] * (lenv) for i in range(lenv)]

  for i in range(lenv, -1, -1):
    for j in range(i, lenv):
      if j == i:
        memo[i][j] = coins[i]
      elif j == i+1:
        memo[i][j] = max(coins[i], coins[j])
      else:
        a = memo[i+2][j] if 0 <= i+2 < lenv and 0 <= j < lenv else 0
        b = memo[i+1][j-1] if 0 <= i+1 < lenv and 0 <= j-1 < lenv else 0
        c = memo[i][j-2] if 0 <= i < lenv and 0 <= j-2 < lenv else 0
        # Even the following should work
        # a = memo[i+2][j]
        # b = memo[i+1][j-1]
        # c = memo[i][j-2]
        # print(a, b, c)
        memo[i][j] = max(
          (coins[i] + min(a, b)),
          (coins[j] + min(b, c))
        )
  return memo[0][lenv-1]


if __name__ == '__main__':
  v = [8, 15, 3, 7]  # And 22
  v = [6, 9, 1, 2, 16, 8] # Ans 23
  v = [ 2, 2, 2, 2]  # Ans 4
  v = [ 20, 30, 2, 2, 2, 10] # ans 42
  print(maxWin(v))
