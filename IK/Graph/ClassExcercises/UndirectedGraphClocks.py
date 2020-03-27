class UndirectedGraphClocks:
  def __init__(self, vertices, edges):
    self.adj_map = self.adjacency_map(vertices, edges)
    self.time = 0
    self.visited = {}

  def adjacency_map(self, vertices, edges):
    # here we keep the neighbour info in an hashset and vertices in an hashmap
    adj_map = {}
    for vertex in vertices:
      adj_map.setdefault(vertex, set())
    for edge_row, edge_col in edges:
      adj_map[edge_row].add(edge_col)
      adj_map[edge_col].add(edge_row)
    return adj_map

  def dfs(self, vertex):
    self.time += 1
    self.visited[vertex] = [self.time, None]
    for neighbor in self.adj_map[vertex]:
      if neighbor not in self.visited:
          self.dfs(neighbor)
    self.time += 1
    self.visited[vertex][1] = self.time

  def explore_graph_dfs(self):
    self.time = 0
    for vertex in self.adj_map.keys():
      if vertex not in self.visited:
        self.dfs(vertex)
    return self.visited

if __name__ == '__main__':
  vertices = [0, 1, 2, 3, 4, 5, 6, 7]
  edges = [[0, 1], [1, 2], [2, 4], [4, 3], [3, 0], [3, 2], [6, 5]]
  sol = UndirectedGraphClocks(vertices, edges)
  print(sol.explore_graph_dfs())
