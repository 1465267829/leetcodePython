"""
https://leetcode.com/problems/k-closest-points-to-origin/

973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

from typing import *
from math import pow, sqrt


# class Solution:
#   def lomuto_partition(self, nums, start, end):
#     less = start
#     for more in range(start+1, end+1):
#       if nums[more][0] <= nums[start][0]:
#         # treat the 0th element element of element as index
#         less += 1
#         nums[less], nums[more] = nums[more], nums[less]
#     nums[less], nums[start] = nums[start], nums[less]
#     return less
#
#   def distance_from_origin(self, a, b=(0, 0)):
#     return sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
#
#   def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#     distances = []
#     for index, point in enumerate(points):
#       distance = self.distance_from_origin(point)
#       distances.append([distance, index])
#
#     start, end = 0, len(distances)-1
#     kth_closest_index = K-1
#     while start <= end:
#       pivot_index = self.lomuto_partition(distances, start, end)
#       if kth_closest_index == pivot_index:
#         result = [points[distances[i][1]] for i in range(pivot_index+1)]
#         return result
#       elif kth_closest_index < pivot_index:
#         end = pivot_index-1
#       else:
#         start = pivot_index+1
#     return -1

class Solution:
  def lomuto_partition(self, nums, start, end):
    less = start
    for more in range(start+1, end+1):
      if nums[more][0] <= nums[start][0]:
        # treat the 0th element element of element as index
        less += 1
        nums[less], nums[more] = nums[more], nums[less]
    nums[less], nums[start] = nums[start], nums[less]
    return less

  def distance_from_origin(self, a, b=(0, 0)):
    return sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))

  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    distances = []
    for index, point in enumerate(points):
      distance = self.distance_from_origin(point)
      distances.append([distance, index])

    start, end = 0, len(distances)-1
    kth_closest_index = K-1
    while start <= end:
      pivot_index = self.lomuto_partition(distances, start, end)
      if kth_closest_index == pivot_index:
        result = [points[distances[i][1]] for i in range(pivot_index+1)]
        return result
      elif kth_closest_index < pivot_index:
        end = pivot_index-1
      else:
        start = pivot_index+1
    return -1

if __name__ == '__main__':
  nums, k = [[3,3],[5,-1],[-2,4]], 2
  # nums, k = [[1,3],[-2,2]], 1
  sol = Solution()
  print(sol.kClosest(nums, k))