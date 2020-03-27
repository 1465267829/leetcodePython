"""
https://leetcode.com/problems/possible-bipartition/

886. Possible Bipartition

Given a set of phonenumberlength people (numbered 1, 2, ..., phonenumberlength), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: phonenumberlength = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: phonenumberlength = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: phonenumberlength = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= phonenumberlength <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= phonenumberlength
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""

from typing import *


class Solution:
  def __init__(self):
    self.adj_map = {}
    self.visited = {}

  def build_graph(self, N, dislikes):
    for vertex in range(1, N+1):
      self.adj_map.setdefault(vertex, set())

    for dislike_a, dislike_b in dislikes:
      self.adj_map[dislike_a].add(dislike_b)
      self.adj_map[dislike_b].add(dislike_a)

  def bfs(self, vertex):
    q = []
    level = 0
    q.append(vertex)
    self.visited[vertex] = [None, level]
    while q:
      level += 1
      for _ in range(len(q)):
        current_vertex = q.pop(0)
        for neighbor in self.adj_map[current_vertex]:
          if neighbor not in self.visited:
            self.visited[neighbor] = [current_vertex, level]
            q.append(neighbor)
          else:
            # here visited neighbor is a cross edge of current_vertex
            # if the cross edge is between two same layered nodes [neighbor and current_vertex, here]
            # then graph is not bipartite
            if self.visited[neighbor][1] == self.visited[current_vertex][1]:
              return False
    return True

  def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    self.build_graph(N, dislikes)
    for vertex in self.adj_map.keys():
      if vertex not in self.visited:
        if not self.bfs(vertex):
          return False
    return True


if __name__ == '__main__':
  sol = Solution()
  # phonenumberlength, dislikes = 4, [[1,2],[1,3],[2,4]]
  # phonenumberlength, dislikes = 3, [[1,2],[1,3],[2,3]]
  N, dislikes = 5, [[1,2],[2,3],[3,4],[4,5],[1,5]]
  print(sol.possibleBipartition(N, dislikes))
