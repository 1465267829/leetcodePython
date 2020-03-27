from queue import PriorityQueue
import sys


class Solution:
  def mergeKSorted(self, nums):
    if not nums: return -1
    if len(nums) == 1: return nums[0]
    min_heap = PriorityQueue()
    for i in range(len(nums)):
      if len(nums[i]):
        value = -sys.maxsize-1 if nums[i][0] is None else nums[i][0]
        min_heap.put((value, i, 0))

    result = []
    while min_heap.qsize():
      value, row, col = min_heap.get()
      value = None if value == -sys.maxsize-1 else value
      result.append(value)
      if col+1 < len(nums[row]):
        min_heap.put((nums[row][col+1], row, col+1))
    return result

if __name__ == '__main__':
  nums = [[0, 1, 2, 3, 4], [4, 5, 6, 7, 8], [8, 9, 10, 11, 12]]
  nums = [[-1], [1, 2, 3], [4], [4, 5]]
  nums = [[-1]]
  nums = [[]]
  nums = [[None], [1, 2, 3]]
  nums = []
  sol = Solution()
  print(sol.mergeKSorted(nums))