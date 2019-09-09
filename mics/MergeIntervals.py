class Solution(object):
  def overlap(self, interval_0, interval_1):
    return (interval_0[0] <= interval_1[0] <= interval_0[1])

  def merged(self, interval_0, interval_1):
      return interval_0 if interval_1[1] < interval_0[1] else [interval_0[0], interval_1[1]]


  def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals: return []

    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    stack = []
    stack.append(sorted_intervals[0])
    for i in range(1, len(sorted_intervals)):
      current_interval = sorted_intervals[i]
      element_to_insert = None
      if self.overlap(stack[-1], current_interval):
        last_interval = stack.pop()
        element_to_insert = self.merged(last_interval, current_interval)
      else:
        element_to_insert = current_interval
      stack.append(element_to_insert)
    return stack

if __name__ == '__main__':
    intervals = [[15,18],[1,3],[2,6],[8,10]]
    # intervals = [[1,4],[2,3]]
    sol = Solution()
    print sol.merge(intervals)