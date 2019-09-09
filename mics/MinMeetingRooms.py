'''
https://leetcode.com/problems/meeting-rooms-ii/solution/
253. Meeting Rooms II
Medium

1598

27

Favorite

Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution(object):
  def overlap(self, left, right):
    if left[0] <= right[0] < left[1]: return True
    return False

  def minMeetingRooms(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals: return 0
    sorted_intervals = sorted(intervals, key=lambda interval:interval[0])
    rooms = []
    rooms.append(sorted_intervals[0])
    for interval_index in range(1, len(sorted_intervals)):
      found_room = False
      for room_index in range(len(rooms)):
        if not self.overlap(rooms[room_index], sorted_intervals[interval_index]):
          rooms[room_index] = sorted_intervals[interval_index]
          found_room = True
      if not found_room: rooms.append(sorted_intervals[interval_index])
    return len(rooms)

if __name__ == '__main__':
  sol = Solution()
  # print(sol.minMeetingRooms( [[0, 30],[5, 10],[15, 20]] ))
  # print(sol.minMeetingRooms( [[7,10],[2,4]] ))
  # print(sol.minMeetingRooms( [[1,5],[8,9],[8,9]] ))
  print(sol.minMeetingRooms( [[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]] ))
