"""
https://leetcode.com/problems/is-graph-bipartite/

785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one current in A and another current in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each current is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""
from typing import *


class Solution:
  def __init__(self):
    self.adj_list = None
    self.visited = {}

  def build_graph(self, graph):
    self.adj_list = graph

  def bfs(self, vertex):
    q = []
    level = 0
    q.append(vertex)
    self.visited[vertex] = [None, level]
    while q:
      level += 1
      for _ in range(len(q)):
        current_vertex = q.pop(0)
        for neighbor in self.adj_list[current_vertex]:
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

  def isBipartite(self, graph: List[List[int]]) -> bool:
    self.build_graph(graph)
    for vertex in range(len(graph)):
      if vertex not in self.visited:
        if not self.bfs(vertex):
          return False
    return True


if __name__ == '__main__':
  sol = Solution()
  graph = [[1,3], [0,2], [1,3], [0,2]]
  graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
  print(sol.isBipartite(graph))
