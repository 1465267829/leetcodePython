'''
https://leetcode.com/problems/hamming-distance/
461. Hamming Distance

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''

class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    text1, text2 = '{0:032b}'.format(x), '{0:032b}'.format(y)
    memo = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for i in range(len(memo)):
      for j in range(len(memo[0])):
        if i == 0 and j == 0:
          memo[i][j] = 0
        elif i == 0:
          memo[i][j] = j
        elif j == 0:
          memo[i][j] = i
        elif text1[i - 1] == text2[j - 1]:
          memo[i][j] = memo[i - 1][j - 1]
        elif text1[i - 1] != text2[j - 1]:
          memo[i][j] = 1 + memo[i - 1][j - 1]  # sub
        else:
          print 'Error'
    return memo[-1][-1]