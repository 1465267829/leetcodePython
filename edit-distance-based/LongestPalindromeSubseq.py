'''
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

'''

# class Solution(object):
#   def memo(self, s):
#     return [[None] * len(s) for i in range(len(s))]
#
#   def helper(self, s, i, j, memo):
#     if memo[i][j]: return memo[i][j]
#     if i == j:
#       memo[i][j] = 1
#     elif i + 1 == j and s[i] == s[j]:
#       memo[i][j] = 2
#     elif s[i] == s[j]:
#       memo[i][j] = 2 + self.helper(s, i + 1, j - 1, memo)
#     else:
#       memo[i][j] = max(self.helper(s, i + 1, j, memo),
#                        self.helper(s, i, j - 1, memo))
#     return memo[i][j]
#
#   def longestPalindromeSubseq(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     if len(s) == 0: return 0
#     if len(s) == 1: return 1
#     memo = self.memo(s)
#     return self.helper(s, 0, len(s) - 1, memo)


class Solution(object):
  def helper(self, s, i, j, memo):
    if (i,j) in memo: return memo[(i,j)]
    if i == j:
      memo[(i,j)] = 1
    elif i + 1 == j and s[i] == s[j]:
      memo[(i,j)] = 2
    elif s[i] == s[j]:
      memo[(i, j)] = 2 + self.helper(s, i + 1, j - 1, memo)
    else:
      memo[(i, j)] = max(self.helper(s, i + 1, j, memo), self.helper(s, i, j - 1, memo))
    return memo[(i, j)]

  def longestPalindromeSubseq(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    res = self.helper(s, 0, len(s) - 1, {})
    return res

if __name__ == '__main__':
  sol = Solution()
  s = 'bbbab'
  print(sol.longestPalindromeSubseq(s))