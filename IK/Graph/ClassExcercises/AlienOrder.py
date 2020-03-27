"""
https://leetcode.com/problems/alien-dictionary/description/

269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from typing import *


class Solution:
  def __init__(self):
    self.adj_map = {}
    self.result = []
    self.time = None
    self.visited = None

  def buildGraph(self, words):
    """
    Here we are working with a graph with vertices being each
    alphabet of alien language
    The directed edges denotes vertex at the source of directed edge
    comes 'before' vertex at the destination of directed edge

    The graph generated is represented as adjacency map.

    To build adjacency map we need to:
    1.Discover vertices:
      Here we take all the non duplicate chars across all the words
      given to us and consider them as vertices

    2.Discover edges:
      As Ganesh explained, we walk each consecutive words from left to right.
      While walking in lock step character by character across consecutive
      words, we try to find which index across both the words have different
      characters while their prefixes being equal.
      Once we have found such a pair of characters then we know that the
      character from previous word comes 'before' character of current word
      For example:
      if previous word is 'wrt' and current word is 'wrf',
      we find the 1st differences at chars ar index 2 denoting 't' from previous
      word and 'f' from current word with their prefixes 'wr' being equal
      This information tells us that in alien language 't' comes before 'f'
      This is modelled in the graph as an directional edge 't' --> 'f'

    Once we have discovred all the vertices and all the edgee, we build adjacency map
    """
    vertices = set(''.join(words))
    edges = []

    for i in range(1, len(words)):
      prev_word, curr_word = words[i-1], words[i]
      prev_word_index, curr_word_index = 0, 0
      while 0 <= prev_word_index < len(prev_word) and 0 <= curr_word_index < len(curr_word):
        if prev_word[prev_word_index] == curr_word[curr_word_index]:
          prev_word_index += 1
          curr_word_index += 1
          continue
        edge = [prev_word[prev_word_index], curr_word[curr_word_index]]
        edges.append(edge)
        break

    # build graph
    for vertex in vertices:
      self.adj_map.setdefault(vertex, set())

    for edge_src, edge_dst in edges:
      self.adj_map[edge_src].add(edge_dst)

  def dfs(self, vertex):
    self.time += 1
    self.visited[vertex] = [self.time, None]
    for neighbor in self.adj_map[vertex]:
      if neighbor not in self.visited:
        if not self.dfs(neighbor):
          # One of our decedents found a cycle
          # return False
          return False
      else:
        # Here we found a back edge indicating cycle
        # topological sort is not possible return False
        # to convey parents and ancestors that we found a cycle
        if not self.visited[neighbor][1]:
          return False
    pass
    self.time += 1
    self.visited[vertex][1] = self.time
    self.result.append(vertex)
    return True

  def topo_sort(self):
    self.visited = {}
    self.time = 0
    for vertex in self.adj_map.keys():
      if vertex not in self.visited:
        if not self.dfs(vertex):
          # Cycle found in the graph
          self.result = []
          return
    self.result.reverse()

  def alienOrder(self, words: List[str]) -> str:
    self.buildGraph(words)
    self.topo_sort()
    return ''.join(self.result)


if __name__ == '__main__':
  sol = Solution()
  words =[
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
  ]
  words = [
    "z",
    "x",
    "z"
  ]
  words = [
    "z",
    "x"
  ]
  words = [
    "z",
    "z"
  ]
  print(sol.alienOrder(words))

