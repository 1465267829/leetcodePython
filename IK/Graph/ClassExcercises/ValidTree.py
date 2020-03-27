"""
https://leetcode.com/problems/graph-valid-tree/

261. Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

https://www.geeksforgeeks.org/check-given-graph-tree/
An undirected graph is tree if it has following properties.
1) There is no cycle.
2) The graph is connected.

1st using DFS
2nd using BFS
"""
from typing import *


class Solution:
  def __init__(self):
    self.adj_map = None
    self.visited = {}

  def build_graph(self, n, edges):
    self.adj_map = {}
    for vertex in range(n):
      self.adj_map.setdefault(vertex, set())
    for edge_src, edge_dst in edges:
      self.adj_map[edge_src].add(edge_dst)
      self.adj_map[edge_dst].add(edge_src)

  def dfs(self, vertex):
    for neighbor in self.adj_map[vertex]:
      if neighbor not in self.visited:
        self.visited[neighbor] = vertex
        if not self.dfs(neighbor):
          return False
      else:
        # if visited neighbour is not parent then we have a back edge
        # back edge indicates cycle
        if self.visited[vertex] != neighbor:
          return False
    return True

  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    self.build_graph(n, edges)
    connected = 0
    for vertex in self.adj_map.keys():
      if vertex not in self.visited:
        if connected >= 1:
          return False
        connected += 1
        self.visited[vertex] = None
        if not self.dfs(vertex):
          return False
    return True

# class Solution:
#   def __init__(self):
#     self.adj_map = None
#     self.visited = {}
#
#   def build_graph(self, n, edges):
#     self.adj_map = {}
#     for vertex in range(n):
#       self.adj_map.setdefault(vertex, set())
#     for edge_src, edge_dst in edges:
#       self.adj_map[edge_src].add(edge_dst)
#       self.adj_map[edge_dst].add(edge_src)
#
#   def bfs(self, vertex):
#     # we launch bfs on the adjacency map
#     q = [vertex]
#     hop = 0
#     self.visited[vertex] = None
#     while q:
#       hop += 1
#       for _ in range(len(q)):
#         current_vertex = q.pop(0)
#         for neighbor in self.adj_map[current_vertex]:
#           if neighbor not in self.visited:
#             self.visited[neighbor] = current_vertex
#             q.append(neighbor)
#           else:
#             if neighbor != self.visited[current_vertex]:
#               return False
#     return True
#
#   def validTree(self, n: int, edges: List[List[int]]) -> bool:
#     self.build_graph(n, edges)
#     connected = 0
#     for vertex in self.adj_map.keys():
#       if vertex not in self.visited:
#         if connected >= 1:
#           return False
#         connected += 1
#         if not self.bfs(vertex):
#           return False
#     return True


if __name__ == '__main__':
  sol = Solution()
  n, edges = 5,  [[0,1], [0,2], [0,3], [1,4]]
  # n, edges = 5,  [[0,1], [1,2], [2,3], [1,3], [1,4]]
  # n, edges = 3,  [[0,1],[0,2],[1,2]]
  print(sol.validTree(n, edges))

