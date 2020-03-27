"""
Merge Sort [Stable sort]

1.  Merge routine is the key. Merge routine takes two sorted lists and merges them into a single sorted list and
    returns such a sorted list.
2.  Merge routine uses auxiliary space to keep the merged list before returning it to the user
3.  Merge routine works in the following way
    1.  Navigate each element in the sorted lists
    2.  Find the smallest of the current elements in each list and add that to the aux list and prop the
        next element of the list for next compare
    3.  Once one list is consumed, iterate the other list and add all the remaining sorted elements to aux list.
    4. Return the aux list.
4.  Mergesort uses merge routine in following two ways:
    1.  Bottoms Up:
        1.  Put each element of the given unsorted array as a single element array in the queue
        2.  Pull 2 'single element' arrays [which are considered trivially sorted] from the queue and ask merge routine
            to merge these two sorted array and return a single sorted array
        3.  Such a single sorted array is them appended to end of the queue.
        4.  This process repeats till queue is left only one element.
        5.  That last element is the sorted list.
        6.  Invariant here is that queue always keeps sorted arrays.
    2.  Top down:
        1.  Use recursion to divide the list into constituent elements.
        2.  Recursion stops at dividing the list till the list has exactly 1 element [which are considered trivially sorted]
        3.  Recursion is made to keep the start and end index only rather than keeping the entire subarray.
        3.  Merge routine in this case gets an array where start to mid is independently sorted and mid to end is
            independently sorted.
        4.  Merge merges such [0, mid] and [mid+1, end] subarrays into one sorted array in place.

Omkar's video link
https://youtu.be/JPfANyP-lzg

"""

from queue import Queue


class MergeSort:
  def merge(self, left, right):
    left_index, right_index, aux = 0, 0, []
    while 0 <= left_index < len(left) and 0 <= right_index < len(right):
      if left[left_index] == right[right_index]:
        aux.append(left[left_index])
        aux.append(right[right_index])
        left_index += 1
        right_index += 1
      elif left[left_index] < right[right_index]:
        aux.append(left[left_index])
        left_index += 1
      else:
        aux.append(right[right_index])
        right_index += 1

    while 0 <= left_index < len(left):
      aux.append(left[left_index])
      left_index += 1

    while 0 <= right_index < len(right):
      aux.append(right[right_index])
      right_index += 1
    return aux

  def sort_top_down_divide_and_conquer(self, nums):
    def helper(nums, start, end):
      if start >= end: return
      mid = start + ((end - start) // 2)
      helper(nums, start, mid)
      helper(nums, mid + 1, end)

      # Merge
      i, j, aux = start, mid + 1, []
      while i <= mid and j <= end:
        if nums[i] <= nums[j]:
          aux.append(nums[i])
          i += 1
        else:
          aux.append(nums[j])
          j += 1

      while i <= mid:
        aux.append(nums[i])
        i += 1

      while j <= end:
        aux.append(nums[j])
        j += 1

      for k in range(start, end + 1): nums[k] = aux.pop(0)
      return nums

    if not nums or len(nums) == 1: return nums
    return helper(nums, 0, len(nums) - 1)

  def sort_bottom_up_divide_and_conquer(self, nums):
    queue = Queue()
    for _, val in enumerate(nums): queue.put([val])
    while queue.qsize() > 1:
      left, right = queue.get(), queue.get()
      queue.put(self.merge(left, right))
    return queue.get()


if __name__ == '__main__':
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  # nums = [9, 8, 7, 6, 9, 4, 3, 2, 1, 0]
  # nums = [0]
  # nums = [-1, -1]
  sol = MergeSort()
  # print(sol.sort_top_down_divide_and_conquer(nums))
  print(sol.sort_bottom_up_divide_and_conquer(nums))
  # print(sol.merge_sort(nums))
