"""
Quick Sort [Unstable sort]

1.  Use partitioning to do the sorting
2.  Following is how it works:
    1. Choose a random index in the given unsorted list
    2. Swap the element at the random index with element at index 0 [or last index, doesn't matter]
    3. Try partitioning all the elements in the array between 1 and last index
    4. Partitioning is done by use lomuto's or hoare's partitioning method
    5. In both the schemes after partitioning is done in such a way that we know an index in the array between 1 and
       last index [called magic_index] where all the element between 1 and including magic_index are less than element
       at index 0 and all the elements between magic_index+1 and end have values more than element at index 0
    6. We then swap the element at index magic_index and index 0.
    7. At this point element in the magic index had found it's place in the overall array if it were to be sorted.
       Omkar described it as bird falling into the final index.
    8. We repeat the steps from 1 to 6 with subarrays on left of magic_index and array on right of magic_index to sort
      the array or have one element in the array which is trivially sorted.
    9. There as some interesting uses of this bird falling property:
       a. If we are finding the nth smallest index in the array and n is less than magic_index then we can discard the
          right subarray and just recurse in the left and vice versa. This way of finding nth smallest is mentioned in
          Dasgupta book.

    Partitioning algo:
    Both the following algorithms take an array and a pivot value.
    They return the rearranged array and magic_index in the rearranged array such that all the elements in the
    array on magic_index and left are less than pivot value and all the elements on the right of the magic index in
    the rearranged array are greater than the pivot value.

    1.Lomuto:Traverse the array and segregate the element as we go from left to right.
    2.Hoare: Have a left and right pointer and do the swaps

Omkar's video link
https://youtu.be/-B4pgL-ZEPU
"""

import random


from random import randrange
from typing import *


class Solution:
  def lomuto_partitioning(self, nums, start, end):
    pivot = randrange(start, end)
    pivot_num = nums[pivot]
    nums[pivot], nums[start] = nums[start], nums[pivot]
    less = start
    for more in range(less, end + 1):
      if nums[more] < pivot_num:
        less += 1
        nums[less], nums[more] = nums[more], nums[less]
    nums[start], nums[less] = nums[less], nums[start]
    return less

  def hoare_partitioning(self, nums, start, end):
    """
    From quick sort wiki
    Hoare's scheme is more efficient than Lomuto's partition scheme because it does three times fewer swaps on average,
    and it creates efficient partitions even when all values are equal.

    Important:

    1. In this scheme, the pivot's final location is not necessarily at the index that was returned.
    2. That's why the next two segments that the main algorithm recurs on are (lo..p) and (p+1..hi)
       as opposed to (lo..p-1) and (p+1..hi) as in Lomuto's scheme.
    3. However, the partitioning algorithm guarantees lo ≤ p < hi which implies both resulting partitions are non-empty,
       hence there's no risk of infinite recursion.
    """
    random_index = randrange(start, end)
    pivot = nums[random_index]
    left, right = start, end
    while True:
      while nums[left] < pivot : left += 1
      while nums[right] > pivot : right -= 1
      if left >= right: break
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
    return right

  def helper(self, nums, start, end):
    if start < end:
      # hoare paritioning
      pivot_index = self.hoare_partitioning(nums, start, end)
      # note the split as compared to lomuto's partition
      self.helper(nums, start, pivot_index)
      self.helper(nums, pivot_index+1, end)

      # lomuto's partitioning
      # pivot_index = self.lomuto_partitioning(nums, start, end)
      # self.helper(nums, start, pivot_index-1)
      # self.helper(nums, pivot_index+1, end)
    return nums

  def sortArray(self, nums: List[int]) -> List[int]:
    return self.helper(nums, 0, len(nums)-1)


if __name__ == '__main__':
  # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  # nums = [9, 8, 7, 6, 9, 4, 3, 2, 0, 0]
  # nums = [0]
  nums = [-1, -1]
  # nums = []
  nums = [9, 8, 7, 7, 5, 5, 1, 2, 3]
  sol = Solution()
  # print(sol.sort(nums))
  print(sol.sortArray(nums))