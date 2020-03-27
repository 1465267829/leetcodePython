"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
from typing import *


class Solution:
  def __init__(self):
    self.adj_map = None
    self.visited = set()

  def build_graph(self, n, edges):
    self.adj_map = {}
    for vertex in range(n):
      self.adj_map.setdefault(vertex, set())
    for edge_src, edge_dst in edges:
      self.adj_map[edge_src].add(edge_dst)
      self.adj_map[edge_dst].add(edge_src)

  def dfs(self, vertex):
    self.visited.add(vertex)
    for neighbor in self.adj_map[vertex]:
      if neighbor not in self.visited:
        self.visited.add(vertex)
        self.dfs(neighbor)

  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    self.build_graph(n, edges)
    connected = 0
    for vertex in self.adj_map.keys():
      if vertex not in self.visited:
        connected += 1
        self.dfs(vertex)
    return connected