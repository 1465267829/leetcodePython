#!/bin/python3

import sys
import os

sys.setrecursionlimit(101000)

class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []


def build_other_graph(node):
  def bfs(vertex):
      # we launch bfs on the adjacency map
      q = [vertex]
      visited[vertex] = None
      while q:
        current_vertex = q.pop(0)
        for neighbor in current_vertex.neighbours:
          if neighbor not in visited:
            visited[neighbor] = current_vertex
            q.append(neighbor)
            if neighbor.val not in transpose:
              transpose[neighbor.val] = set()
            transpose[neighbor.val].add(current_vertex.val)
          else:
            if neighbor.val not in transpose:
              transpose[neighbor.val] = set()
            transpose[neighbor.val].add(current_vertex.val)

  transpose = {}
  visited = {}
  bfs(node)
  handle = None
  temp = {}
  if not transpose:
    return node
  for vertex in transpose.keys():
    node = Node()
    node.val = vertex
    node.neighbours = []
    temp[vertex] = node

  for vertex in transpose.keys():
    node = temp[vertex]
    if not handle:
      handle = node
    for neighbor in transpose[vertex]:
      node.neighbours.append(temp[neighbor])
  return handle


reversed = {}


def helper_dfs(reversed_node):
  reversed[reversed_node.val] = reversed_node
  n = len(reversed_node.neighbours)
  for i in range(0, n):
    if not reversed_node.neighbours[i].val in reversed:
      helper_dfs(reversed_node.neighbours[i])


def helper_get_all_addresses_in_reversed_graph(reversed_node):
  helper_dfs(reversed_node)
  return reversed


def helper(graph_nodes, graph_from, graph_to):
  # ----
  MAX_NODES = 315
  # ----

  original = {}
  for i in range(1, graph_nodes + 1):
    node = Node()
    node.val = i;
    original[i] = node
  edges = {}

  graph_edges = len(graph_from)
  for i in range(0, graph_edges):
    original[graph_from[i]].neighbours.append(original[graph_to[i]])
    edges[MAX_NODES * (graph_from[i] - 1) + graph_to[i] - 1] = True

  # Student will return only one current. Do a dfs and get all the nodes.
  reversed = helper_get_all_addresses_in_reversed_graph(build_other_graph(original[1]))

  sys.stderr.write("In returned graph: \n")
  for val in reversed.keys():
    sys.stderr.write("Neighbours of current " + str(val) + " = [")
    node = reversed[val]
    n = len(node.neighbours)
    for i in range(0, n):
      _val = node.neighbours[i].val
      sys.stderr.write(str(_val))
      if i != n - 1:
        sys.stderr.write(", ")
    sys.stderr.write("]\n")

  if (len(reversed) != graph_nodes):
    sys.stderr.write("Wrong answer because no of nodes in returned graph != no of nodes in original graph.\n")
    return "Wrong Answer!"

  for val in reversed.keys():
    node = reversed[val]
    if 1 > val or val > graph_nodes:
      sys.stderr.write("Wrong answer because value of current is out of range.\n")
      return "Wrong Answer!"
    # New graph should not contain current from original graph.
    if original[val] == reversed[val]:
      sys.stderr.write("Wrong answer because instead of creating new current, you have used current from original graph.\n")
      return "Wrong Answer!"
    n = len(node.neighbours)
    for i in range(0, n):
      _val = node.neighbours[i].val
      temp = MAX_NODES * (_val - 1) + val - 1
      if not temp in edges:
        sys.stderr.write("Wrong answer because returned graph contains edge that is not present in original graph.\n")
        return "Wrong Answer!"
      del edges[temp]
  # All the edges should be present in the new graph.
  if len(edges) > 0:
    sys.stderr.write("Wrong answer because returned graph contains extra edge that is not present in original graph\n")
    return "Wrong Answer!"
  return "Correct Answer!"


if __name__ == "__main__":
  f = sys.stdout

  graph_nodes, graph_edges = map(int, input().split())

  graph_from = [0] * graph_edges
  graph_to = [0] * graph_edges

  for graph_i in range(graph_edges):
    graph_from[graph_i], graph_to[graph_i] = map(int, input().split())

  res = helper(graph_nodes, graph_from, graph_to)
  f.write(res + "\n")

  f.close()

