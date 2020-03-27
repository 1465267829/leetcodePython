
from typing import *

# class Solution:
#   def helper(self, current_nums, slate, result, k_slots):
#     if len(slate) == k_slots:
#       result.append(slate[:])
#       return
#     for index, value in enumerate(current_nums):
#       slate.append(value)
#       self.helper(current_nums, slate, result, k_slots)
#       slate.pop()
#
#   def permute(self, nums: List[int]) -> List[List[int]]:
#     current_nums, slate, result = nums, [], []
#     self.helper(current_nums, slate, result, 3)
#     return result

class Solution:
  """
  1.  Generate all permutations with repetition
  2.  # of such permutations are K^N
  3.  Idea is:
      1. Have a slate and list of numbers to pick from to fill the slate [current_nums]
      2. Slate starts with nothing filled and current_nums start with all nums
      3. We then iterate over each element in current_nums and add the element to
         slate.
      4. Terminating condition is if slate has desired number of slots filled in
  4. This is literally what Om describes
  
    # DFS
    # generating string left to right
    # every node other than leaf level does constant work
    # bottom heavy, leaf does most work
  
  If the set S has k elements, the number of n-tuples over S is the result returned
  """

  def helper(self, nums, index, slate, result, num_slots):
    # base
    if len(slate) == num_slots:
      result.append(slate[:])
      return

    for current_index in range(index, len(nums)):
      slate.append(nums[current_index])
      self.helper(nums, index, slate, result, num_slots)
      slate.pop()

  def permute(self, nums: List[int]) -> List[List[int]]:
    index, slate, result, num_slots = 0, [], [], len(nums)
    self.helper(nums, index, slate, result, num_slots)
    return result


if __name__ == '__main__':
  sol = Solution()
  nums = [1, 2, 3]
  print(sol.permute(nums))
