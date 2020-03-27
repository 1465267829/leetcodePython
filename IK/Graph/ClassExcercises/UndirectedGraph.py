class UndirectedGraph:
  def __init__(self, vertices, edges):
    self.adj_matrix = self.adjacency_matrix(vertices, edges)
    self.adj_list = self.adjacency_list(vertices, edges)
    self.adj_map = self.adjacency_map(vertices, edges)
    self.time = 0

  def adjacency_matrix(self, vertices, edges):
    adj_matrix = [[None] * len(vertices) for _ in range(len(vertices))]
    for edge_row, edge_col in edges:
      adj_matrix[edge_row][edge_col] = 1
      adj_matrix[edge_col][edge_row] = 1
    return adj_matrix

  def adjacency_list(self, vertices, edges):
    # here we keep the neighbour info in an array and vertices in an array
    adj_list = [[] for _ in range(len(vertices))]
    for edge_row, edge_col in edges:
      adj_list[edge_row].append(edge_col)
      adj_list[edge_col].append(edge_row)
    return adj_list

  def adjacency_map(self, vertices, edges):
    # here we keep the neighbour info in an hashset and vertices in an hashmap
    adj_map = {}
    for vertex in vertices:
      adj_map.setdefault(vertex, set())
    for edge_row, edge_col in edges:
      adj_map[edge_row].add(edge_col)
      adj_map[edge_col].add(edge_row)
    return adj_map

  def bfs(self, vertex, visited=None):
    # we launch bfs on the adjacency map
    if not visited:
      visited = {}
    q = [vertex]
    hop = 0
    visited[vertex] = [None, hop]
    while q:
      hop += 1
      for _ in range(len(q)):
        current_vertex = q.pop(0)
        for neighbor in self.adj_map[current_vertex]:
          if neighbor not in visited:
            visited[neighbor] = [current_vertex, hop]
            q.append(neighbor)
    return visited

  def explore_graph_bfs(self):
    visited = {}
    for vertex in self.adj_map.keys():
      if vertex not in visited:
        visited = self.bfs(vertex, visited)
    return visited

  def dfs_iterative(self, vertex):
    # we launch dfs on the adjacency map
    visited = {}
    q = [vertex]
    visited[vertex] = None
    while q:
      for _ in range(len(q)):
        current_vertex = q.pop()
        for neighbor in self.adj_map[current_vertex]:
          if neighbor not in visited:
            visited[neighbor] = current_vertex
            q.append(neighbor)
    return visited

  def dfs(self, vertex, visited=None):
    def dfs_helper(vertex):
      for neighbor in self.adj_map[vertex]:
        if neighbor not in visited:
          visited[neighbor] = vertex
          dfs_helper(neighbor)

    if not visited: visited = {}
    visited[vertex] = None
    dfs_helper(vertex)
    return visited

  def explore_graph_dfs(self):
    visited = {}
    for vertex in self.adj_map.keys():
      if vertex not in visited:
        visited = self.dfs(vertex, visited)
    return visited


if __name__ == '__main__':
  vertices = [0, 1, 2, 3, 4, 5, 6, 7]
  edges = [[0, 1], [1, 2], [2, 4], [4, 3], [3, 0], [3, 2], [6, 5]]
  sol = UndirectedGraph(vertices, edges)
  # print(sol.bfs(0))
  # print(sol.explore_graph_bfs())
  # sol.dfs_iterative(0)
  print(sol.dfs(0))
  # print(sol.explore_graph_dfs())