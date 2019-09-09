'''
https://leetcode.com/problems/delete-operation-for-two-strings/
583. Delete Operation for Two Strings
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:

The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''
class Solution(object):
  # def create_memo(self, word1, word2):
  #   memo = []
  #   for i in range(len(word1) + 1):
  #     if i == 0:
  #       memo.append([0] * (len(word2) + 1))
  #     else:
  #       memo.append([0] + [None] * len(word2))
  #   return memo
  #
  # def find_lcs_num(self, word1, word2):
  #   memo = self.create_memo(word1, word2)
  #   for i in range(1, len(memo)):
  #     for j in range(1, len(memo[0])):
  #       if word1[i - 1] == word2[j - 1]:
  #         memo[i][j] = 1 + memo[i - 1][j - 1]
  #       else:
  #         memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])
  #   return memo[-1][-1]
  #
  # def minDistance(self, word1, word2):
  #   """
  #   :type word1: str
  #   :type word2: str
  #   :rtype: int
  #   """
  #   # validate word1 and word2
  #   word1 = "sea"
  #   word2 = "eat"
  #   num_lcs = self.find_lcs_num(word1, word2)
  #   return (len(word1) + len(word2)) - (2 * num_lcs)

  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word1) < len(word2): word1, word2 = word2, word1
    curr = [0] * (len(word2) + 1)
    prev = [0] * (len(word2) + 1)
    for i in range(1, len(word1) + 1):
      for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
          curr[j] = 1 + prev[j - 1]
        else:
          curr[j] = max(prev[j], curr[j - 1])
      prev, curr = curr, prev
    return len(word1) + len(word2) - (2 * prev[-1])

if __name__ == '__main__':
  sol = Solution()
  sol.minDistance()