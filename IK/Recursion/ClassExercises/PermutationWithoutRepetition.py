"""
https://leetcode.com/problems/permutations/

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import *

"""
Following is non optimized and works

class Solution:
  def helper(self, current_nums, slate, result, k_slots):
    if len(slate) == k_slots:
      result.append(slate[:])
      return
    for index, value in enumerate(current_nums):
      slate.append(value)
      self.helper(current_nums[:index] + current_nums[index+1:], slate, result, k_slots)
      slate.pop()

  def permute(self, nums: List[int]) -> List[List[int]]:
    current_nums, slate, result = nums, [], []
    self.helper(current_nums, slate, result, len(nums))
    return result

"""

# Following is better and works


class Solution:
  """
  1.  Problem: Generate all permutations without repetition
  2.  Number of such permutations are P(N,K)
  Idea
  1. Have a slate to track the ongoing combination being generated [slate]
  2. Have a list of available items to choose from
     [items in the list nums between index 'index' to last index <both inclusive>]
  3. In each recursion we do the following:
     Run a for loop picking one item from list of available items
     Add the chosen item to slate
     Delete the chosen item from the list of available items to choose from.
     Recurse on list of available items to choose from and with slate filled with one for choice.
  4. Here the 'list of available items to choose from' could have been passed to next
     recursion after removing the chosen item by concatenation. This is shown the code commented
     above.
  5. Better way is to swap the chosen item into part of num that will not be considered
     in the next iteration.

     We know that the current index 'index' will not be considered in the
     next iteration as we call the next recursion with parameter index+1.

     We use this information to remove the currently chosen item from list of items to be considered
     in next recursion by swapping elements at chosen index [current_index] and index that will
     not be considered in the next recursion [index].

  # DFS
  # generating string left to right
  # every node other than leaf level does constant work
  # bottom heavy, leaf does most work

  Implements P(n,k) Where n are the numbers of elements in set current_nums
  k is the number of elements taken from set current_nums at once to generate
  a permutation
  """
  def helper(self, nums, index, slate, result, k):
    # backtrack
    if len(slate) == k:
      result.append(slate[:])
      return

    # base case
    if index == len(nums):
      result.append(slate[:])
      return

    # recursive case
    for current_index in range(index, len(nums)):
      # choose the element at current_index to be appended to slate
      # then append the chosen element to the slate
      slate.append(nums[current_index])
      # remove the chosen element from being considered in the next recursion
      #
      # we know that next recursion will consider the elements in nums between
      # index+1 and last index.
      # So we swap the chosen element with element at index 'index'.
      #
      # The act of swapping makes ensures that all the elements from current recursion
      # except the chosen one are considered in the next recursion.
      nums[current_index], nums[index] = nums[index], nums[current_index]
      self.helper(nums, index + 1, slate, result, k)
      # undo the swap above to leave nums in state that it entered into this recursion
      # if we don't then all the recursions after us will not be able to
      # assure the order
      nums[current_index], nums[index] = nums[index], nums[current_index]
      # undo the slate
      slate.pop()

  def permute(self, nums: List[int]) -> List[List[int]]:
    index, slate, result, max_slots = 0, [], [], 2
    self.helper(nums, index, slate, result, max_slots)
    return result


if __name__ == '__main__':
  sol = Solution()
  nums = [1, 2, 3, 4, 5]
  ret = sol.permute(nums)
  print(len(ret), ret)
