'''
https://leetcode.com/problems/meeting-rooms/submissions/
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution(object):
  def overlap(self, interval_0, interval_1):
    return False if interval_1[0] >= interval_0[1] else True

  def canAttendMeetings(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: bool
    """
    if not intervals: return True
    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    stack = []
    stack.append(sorted_intervals[0])
    for i in xrange(1, len(sorted_intervals)):
      current_interval = sorted_intervals[i]
      if self.overlap(stack[-1], current_interval):
        return False
      else:
        stack.append(current_interval)
    return True

if __name__ == '__main__':
    # intervals = [[0,30],[5,10],[15,20]]
    # intervals = [[7,10],[2,4]]
    intervals = [[13,15],[1,13]]
    sol = Solution()
    print(sol.canAttendMeetings(intervals))