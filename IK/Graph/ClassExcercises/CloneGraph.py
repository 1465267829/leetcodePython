"""
https://leetcode.com/problems/clone-graph/

133. Clone Graph

Given a reference of a current in a connected undirected graph, return a deep copy (clone) of the graph. Each current in the graph contains a val (int) and a list (List[Node]) of its neighbors.



Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if current p has current q as neighbor, then current q must have current p as neighbor too.
You must return the copy of the given current as a reference to the cloned graph.
"""


# Definition for a Node.
class Node:
  def __init__(self, val, neighbors):
      self.val = val
      self.neighbors = neighbors


class Solution:
  def __init__(self):
    self.dict = {}

  def dfs(self, current):
    for neighbor in current.neighbors:
      if neighbor.val not in self.dict:

        neighbor_clone = Node(neighbor.val, [])
        self.dict[neighbor_clone.val] = neighbor_clone

        self.dict[current.val].neighbors.append(neighbor_clone)
        self.dfs(neighbor)
      else:
        self.dict[current.val].neighbors.append(self.dict[neighbor.val])

  def cloneGraph(self, node: 'Node') -> 'Node':
    new_node = Node(node.val, [])
    self.dict[new_node.val] = new_node
    self.dfs(node)
    return new_node


if __name__ == '__main__':
  sol = Solution()
  node_1 = Node(1, [])
  node_2 = Node(2, [])
  node_1.neighbors.append(node_2)
  node_2.neighbors.append(node_1)

  node_3 = Node(3, [])

  node_3.neighbors.append(node_1)
  node_3.neighbors.append(node_2)
  node_1.neighbors.append(node_3)
  node_2.neighbors.append(node_3)

  ret = sol.cloneGraph(node_1)
  pass