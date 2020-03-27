# https://youtu.be/xWz2_6YlVk0

"""
Increase priority given a node in the heap:
1. Keep swapping value with the parent until reach the top of heap or node has less priority than parent

Decrease priority given a node:
1. Find the largest priority among current node and 0/1/2 children. If 0 child then do nothing
   If 1 or 2 children the find the max priority element among node and children.
   If the node has less priority the do nothing else swap eith child with high priority
   Launch the decrease priority on the swapped self.

Add to heap:
1. Append at the end and increase priority

Delete from heap:
1. Swap the element from last with top
2. Pop and return the last
3. Run decrease priority on the root
"""
class HeapSortMaxHeap:
  """
  Implements a max heap, so sorts in descending order
  Implements heap on 1 based array
  Sort is not in place
  """
  def __init__(self):
    self.heap = []
    self.heap.append(None)

  def parent_index(self, index):
    if index == 1: return None
    return index//2

  def left_child_index(self, index):
    left_index = 2 * index if 2 * index < len(self.heap) else None
    return left_index

  def right_child_index(self, index):
    right_index = (2 * index) + 1 if (2 * index) + 1 < len(self.heap) else None
    return right_index

  def increase_priority(self, index):
    while self.parent_index(index) and self.heap[self.parent_index(index)] < self.heap[index]:
      parent_index = self.parent_index(index)
      self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
      index = parent_index
    pass

  def decrease_priority(self, index):
    while index:
      self_index, left_child_index, right_child_index = index, self.left_child_index(index), self.right_child_index(index)
      # Assume self_index to be the index with largest of three values among self, left child and right child
      largest_index = self_index

      # left child is larger than self
      if left_child_index and self.heap[left_child_index] > self.heap[largest_index]: largest_index = left_child_index
      # right child is larger than largest_index
      if right_child_index and self.heap[right_child_index] > self.heap[largest_index]: largest_index = right_child_index

      if largest_index != self_index:
        # either left or right child is larger
        self.heap[largest_index], self.heap[self_index] = self.heap[self_index], self.heap[largest_index]
        index = largest_index
      else:
        # both left and right child are not larger than self; set index to None to break
        index = None

  def insert_max_heap(self, num):
    self.heap.append(num)
    append_index = len(self.heap) - 1
    self.increase_priority(append_index)

  def extract_max_heap(self):
    if len(self.heap) < 2: return None
    self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
    result = self.heap.pop()
    self.decrease_priority(1)
    return result

  def sort(self, nums):
    for num in nums: self.insert_max_heap(num)
    result = [self.extract_max_heap() for _ in nums]
    return result


class HeapSortMinHeap:
  """
  Implements a min heap, so sorts in ascending order
  Implements heap on 0 based array
  Sort is not in place
  """
  def __init__(self):
    self.heap = []

  def parent_index(self, index):
    if index == 0: return None
    return (index-1)//2

  def left_child_index(self, index):
    left_index = (2*index) + 1
    return left_index if left_index < len(self.heap) else None

  def right_child_index(self, index):
    right_index = (2*index) + 2
    return right_index if right_index < len(self.heap) else None

  def increase_priority(self, index):
    while self.parent_index(index) is not None and self.heap[self.parent_index(index)] > self.heap[index]:
      parent_index = self.parent_index(index)
      self.heap[parent_index],  self.heap[index] = self.heap[index], self.heap[parent_index]
      index = parent_index
    pass

  def decrease_priority(self, index):
    while index is not None:
      self_index, left_child_index, right_child_index = index, self.left_child_index(index), self.right_child_index(index)
      smallest_index = self_index
      if left_child_index is not None and self.heap[left_child_index] < self.heap[smallest_index]: smallest_index = left_child_index
      if right_child_index is not None and self.heap[right_child_index] < self.heap[smallest_index]: smallest_index = right_child_index
      if smallest_index != self_index:
        self.heap[smallest_index], self.heap[self_index] = self.heap[self_index], self.heap[smallest_index]
        index = smallest_index
      else:
        index = None

  def insert_min_heap(self, num):
    self.heap.append(num)
    self.increase_priority(len(self.heap)-1)

  def extract_min_heap(self):
    if not len(self.heap): return None
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    result = self.heap.pop()
    self.decrease_priority(0)
    return result

  def min_heapify(self, nums):
    self.heap = nums[:]
    start, end,  = 0, len(nums)-1
    mid = start+((end-start)//2)
    for i in range(mid, -1, -1): self.decrease_priority(i)

  def sort(self, nums):
    self.min_heapify(nums)
    result = [self.extract_min_heap() for _ in nums]
    return result


if __name__ == '__main__':
  nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  # nums = [9, 8, 7, 6, 9, 4, 3, 2, 0, 0]
  # # nums = [0]
  # nums = [-1, -1]
  # nums = []
  # nums = [-1, -1, -1]

  # sol = HeapSortMaxHeap()
  # for num in nums: sol.insert_max_heap(num)
  # for _ in nums: print(sol.extract_max_heap())
  # print(sol.sort(nums))

  sol = HeapSortMinHeap()
  # for num in nums: sol.insert_min_heap(num)
  # for _ in nums: print(sol.extract_min_heap())
  # print(sol.sort(nums))
  # sol.min_heapify(nums)
  # for _ in nums: print(sol.extract_min_heap())
  print(sol.sort(nums))

