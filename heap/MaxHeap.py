import sys
class MaxHeap(object):
  def __init__(self):
    self.heap = []

  def show(self):
    print self.heap

  def _get_parent_index(self, index):
    parent_index = (index - 1) // 2
    return None if parent_index < 0 else parent_index

  def _get_left_child_index(self, index):
    left_child_index = (2 * index) + 1
    return None if left_child_index >= len(self.heap) else left_child_index

  def _get_right_child_index(self, index):
    right_child_index = (2 * index) + 2
    return None if right_child_index >= len(self.heap) else right_child_index

  def _sift_down(self, index):
    if index == len(self.heap) - 1: return
    left_child_index = self._get_left_child_index(index)
    right_child_index = self._get_right_child_index(index)
    left_child = -sys.maxint - 1 if left_child_index is None else self.heap[left_child_index]
    right_child = -sys.maxint - 1 if right_child_index is None else self.heap[right_child_index]
    largest_element_index = index
    if left_child > self.heap[index]:
      largest_element_index = left_child_index
    if right_child > self.heap[largest_element_index]:
      largest_element_index = right_child_index
    if largest_element_index != index:
      self.heap[largest_element_index], self.heap[index] = self.heap[index], self.heap[largest_element_index]
      self._sift_down(largest_element_index)

  def _sift_up(self, index):
    parent_index = self._get_parent_index(index)
    if parent_index is None: return
    if self.heap[parent_index] <= self.heap[index]:
      self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
      self._sift_up(parent_index)

  def heapify(self, arr):
    self.heap = arr
    for i in range((len(self.heap) // 2) - 1, -1, -1):
      self._sift_down(i)

  def extract_max(self):
    max = None
    if len(self.heap) == 0:
      pass
    elif len(self.heap) == 1:
      max = self.heap[0]
      self.heap = []
    else:
      max = self.heap[0]
      self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
      self.heap.pop()
      self._sift_down(0)
    return max

  def insert(self, key):
    self.heap.append(key)
    self._sift_up(len(self.heap) - 1)

  def merge(self, heap):
    self.heap += heap.heap
    self.heapify(self.heap)

if __name__ == "__main__":
  heap = MaxHeap()
  input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  # heap.heapify(input)
  # for _ in range(len(heap.heap)):
  #   print heap.extract_max(),
  for i in input:
    heap.insert(i)
    if len(heap.heap) > 2:
      heap.extract_max()

  for _ in range(len(heap.heap)):
    print heap.extract_max(),