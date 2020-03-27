"""
https://leetcode.com/problems/course-schedule/

207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
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

  def adjacency_map(self, courses, prerequisites):
    for course in range(courses):
      self.adj_map.setdefault(course, set())
    for prereq_src, prereq_dst in prerequisites:
      self.adj_map[prereq_src].add(prereq_dst)

  def dfs(self, course):
    self.time += 1
    self.visited[course] = [self.time, None]
    for dependent_course in self.adj_map[course]:
      if dependent_course not in self.visited:
        if not self.dfs(dependent_course):
          return False
      else:
        # we are here as we have non tree edge
        if not self.visited[dependent_course][1]:
          # we are here as we found a back edge
          # back edge in dfs suggests cycles
          # if cycle, no degree
          return False
    self.time += 1
    self.visited[course][1] = self.time
    return True

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    self.adjacency_map(numCourses, prerequisites)
    self.time = 0
    for course in self.adj_map.keys():
      if course not in self.visited:
        if not self.dfs(course):
          return False
    return True


if __name__ == '__main__':
  sol = Solution()
  numCourses, prerequisites = 2, [[1, 0]]
  numCourses, prerequisites = 2, [[1,0],[0,1]]
  print(sol.canFinish(numCourses, prerequisites))