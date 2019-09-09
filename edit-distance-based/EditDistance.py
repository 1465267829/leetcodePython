'''
https://www.youtube.com/watch?v=MiqoA-yF-0M
https://www.youtube.com/watch?v=Xxx0b7djCrs

72. Edit Distance
https://leetcode.com/problems/edit-distance/
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    weight_del = 1
    weight_ins = 1
    weight_sub = 1

    # memo = [[0] * (1 + len(word2)) for _ in range(1 + len(word1))]
    # for i in range(len(memo)):
    #   for j in range(len(memo[0])):
    #     if i == 0 and j == 0:
    #       memo[i][j] = 0
    #     elif i == 0:
    #       memo[i][j] = j * weight_del
    #     elif j == 0:
    #       memo[i][j] = i * weight_ins
    #     elif word1[i-1] == word2[j-1]:
    #       memo[i][j] = memo[i-1][j-1]
    #     elif word1[i-1] != word2[j-1]:
    #       memo[i][j] = min(
    #         (weight_del + memo[i-1][j]), # deletion/top
    #         (weight_ins + memo[i][j-1]), # insertion/left
    #         (weight_sub + memo[i-1][j-1])# substitution/diag up left
    #       )
    #     else:
    #       print('we should not be here')
    # print memo
    # return memo[-1][-1]

    if len(word1) <= len(word2): word2, word1 = word1, word2
    curr = [0] * (1 + len(word2))
    prev = [0] * (1 + len(word2))
    for i in range(len(word1) + 1):
      for j in range(len(word2) + 1):
        if i == 0 and j == 0:
          curr[j] = 0
        elif i == 0:
          curr[j] = j * weight_del
        elif j == 0:
          curr[j] = i * weight_ins
        elif word1[i-1] == word2[j-1]:
          curr[j] = prev[j-1]
        elif word1[i-1] != word2[j-1]:
          curr[j] = min(
            (weight_del + prev[j]), # deletion/top
            (weight_ins + curr[j-1]), # insertion/left
            (weight_sub + prev[j-1])# substitution
          )
        else:
          print('we should not be here')
      print curr
      prev, curr = curr, prev
    return prev[-1]

if __name__ == '__main__':
  sol = Solution()
  # word1 = 'horse'
  # word2 = 'ros'
  word1 = 'intention'
  word2 = 'execution'
  print(sol.minDistance(word1, word2))