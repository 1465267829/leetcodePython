'''
1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
'''
class Solution(object):
  def maxUncrossedLines(self, text1, text2):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    if len(text1) < len(text2): text1, text2 = text2, text1
    curr = [0] * (len(text2) + 1)
    prev = [0] * (len(text2) + 1)
    for i in range(1, len(text1) + 1):
      for j in range(1, len(text2) + 1):
        if text1[i - 1] == text2[j - 1]:
          curr[j] = 1 + prev[j - 1]
        else:
          curr[j] = max(prev[j], curr[j - 1])
      prev, curr = curr, prev
    return prev[-1]