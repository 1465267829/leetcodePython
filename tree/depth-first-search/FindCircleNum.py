'''
https://leetcode.com/problems/friend-circles/
547. Friend Circles
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:

N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''
class Solution(object):
  def dfs(self, M, indices):
    (x, y) = indices
    for (p, q) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
    # for (p, q) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1)]:
    # for (p, q) in [(x, y + 1), (x + 1, y + 1), (x + 1, y)]:
      if 0 <= p < len(M) and 0 <= q < len(M) and M[p][q] != 2:
        if M[p][q] == 1:
          M[p][q] = 2
          self.dfs(M, (p, q))
    M[x][y] = 0

  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    circles = 0
    stack = []
    # validate M
    for i in range(len(M)):
      for j in range(len(M[0])):
        if M[i][j] == 1:
          circles += 1
          self.dfs(M, (i, j))
    return circles

if '__main__' == __name__:
  # ans: 2
  # M = [[1,1,0],
  #      [1,1,0],
  #      [0,0,1]]
  # ans: 4
  M = [[1,0,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,1,1]]
  sol = Solution()
  print(sol.findCircleNum(M))