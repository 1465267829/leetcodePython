"""
https://leetcode.com/problems/course-schedule-ii/

210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import *


class Solution:
  def __init__(self):
    self.adj_map = {}
    self.time = 0
    self.visited = {}
    self.toposort = []

  def adjacency_map(self, courses, prerequisites):
    for course in range(courses):
      self.adj_map.setdefault(course, set())
    for prereq_dependent, prereq in prerequisites:
      self.adj_map[prereq].add(prereq_dependent)

  def dfs(self, course):
    self.time += 1
    self.visited[course] = [self.time, None]
    for prereq in self.adj_map[course]:
      if prereq not in self.visited:
        if not self.dfs(prereq):
          return False
      else:
        # we are here as we have non tree edge
        if not self.visited[prereq][1]:
          # we are here as we found a back edge
          # back edge in dfs suggests cycles
          # if cycle, no degree
          return False
    self.time += 1
    self.visited[course][1] = self.time
    self.toposort.append(course)
    return True

  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    self.adjacency_map(numCourses, prerequisites)
    self.time = 0
    for course in self.adj_map.keys():
      if course not in self.visited:
        if not self.dfs(course):
          return []
    self.toposort.reverse()
    return self.toposort


if __name__ == '__main__':
  sol = Solution()
  # numCourses, prerequisites = 2, [[1, 0]]
  numCourses, prerequisites = 2, [[0, 1]]
  # numCourses, prerequisites = 2, [[1,0],[0,1]]
  # numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
  print(sol.findOrder(numCourses, prerequisites))