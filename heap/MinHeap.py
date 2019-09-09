import sys
class MinHeap(object):
  # Min Heap
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

  def _sift_up(self, index):
    parent_index = self._get_parent_index(index)
    if parent_index is None: return
    if self.heap[parent_index] >= self.heap[index]:
      self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
      self._sift_up(parent_index)

  def _sift_down(self, index):
    # also called min_heapify
    if index == len(self.heap) - 1: return
    left_child_index = self._get_left_child_index(index)
    right_child_index = self._get_right_child_index(index)
    left_child = sys.maxint if left_child_index is None else self.heap[left_child_index]
    right_child = sys.maxint if right_child_index is None else self.heap[right_child_index]
    smallest_element_index = index
    if self.heap[smallest_element_index] > left_child:
      smallest_element_index = left_child_index
    if self.heap[smallest_element_index] > right_child:
      smallest_element_index = right_child_index
    if smallest_element_index != index:
      self.heap[smallest_element_index], self.heap[index] = self.heap[index], self.heap[smallest_element_index]
      self._sift_down(smallest_element_index)

  def insert(self, key):
    self.heap.append(key)
    index = len(self.heap) - 1
    self._sift_up(index)

  def find_min(self):
    return self.heap[0]

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

  def heapify(self, arr):
    self.heap = arr
    for i in range((len(self.heap) // 2) - 1, -1, -1):
      self._sift_down(i)

  def heapify_inefficient(self, arr):
    # using shift up, this run though the entire array
    self.heap = arr
    for i in range(len(self.heap) - 1, -1, -1):
      self._sift_up(i)

  def merge(self, heap):
    self.heap += heap.heap
    self.heapify(self.heap)

if __name__ == '__main__':
  heap = MinHeap()
  input = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  input = [3,2,1,5,6,4]
  input = [1]
  for i in input:
    heap.insert(i)
    if len(heap.heap) > 1:
      print heap.extract_min()
  print heap.extract_min()
  heap.show()

  # print heap.show()
  # print heap.extract_min()
  # print heap.show()
  # print heap.extract_min()
  # print heap.extract_min()
  # print heap.show()
  # heap.heapify(input)
  # while True:
  #   val = heap.extract_min()
  #   if val is None: break
  #   print val,
  # heap.show()
  # heap1 = MinHeap()
  # input1 = [5, 4, 3, 2, 1]
  # heap1.heapify(input1)
  # heap2 = MinHeap()
  # input2 = [9, 8, 7, 6]
  # heap2.heapify(input2)
  # heap1.merge(heap2)
  # while True:
  #   val = heap1.extract_min()
  #   if val is None: break
  #   print val,

