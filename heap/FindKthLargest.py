'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''
import sys

class MinHeap(object):
  def __init__(self):
    self.heap = []

  def _sift_down(self, index):
    parent_index = (index - 1) // 2
    left_child_index = (2 * index) + 1
    right_child_index = (2 * index) + 2
    left_child = sys.maxint if left_child_index > (len(self.heap) - 1) else \
    self.heap[left_child_index]
    right_child = sys.maxint if right_child_index > (len(self.heap) - 1) else \
    self.heap[right_child_index]
    smallest_index = index
    if left_child < self.heap[smallest_index]:
      smallest_index = left_child_index
    if right_child < self.heap[smallest_index]:
      smallest_index = right_child_index
    if smallest_index != index:
      self.heap[smallest_index], self.heap[index] = self.heap[index], self.heap[
        smallest_index]
      self._sift_down(smallest_index)

  def extract_min(self):
    min = None
    if len(self.heap) == 0:
      pass
    elif len(self.heap) == 1:
      min = self.heap[0]
      self.heap = []
    else:
      min = self.heap[0]
      self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
      self.heap.pop()
      self._sift_down(0)
    return min

  def _sift_up(self, index):
    parent_index = (index - 1) // 2
    parent_index = None if parent_index < 0 else parent_index
    if parent_index is None: return
    if self.heap[parent_index] >= self.heap[index]:
      self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[
        parent_index]
      self._sift_up(parent_index)

  def insert(self, key):
    self.heap.append(key)
    self._sift_up(len(self.heap) - 1)


class Solution(object):
  def findKthLargest(self, nums, k):
    heap = MinHeap()
    for i in nums:
      heap.insert(i)
      if len(heap.heap) > k: heap.extract_min()
    return heap.extract_min()