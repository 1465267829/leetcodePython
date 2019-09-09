'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.
'''

class Solution(object):
  def findKthSmallest(self, nums, k):
    if k == 1 and len(nums) == 1: return nums[0]
    random_index = len(nums) // 2
    random_num_element = nums[random_index]
    less, equal, greater = [], [], []

    for i in range(len(nums)):
      if nums[i] < random_num_element:
        less.append(nums[i])
      elif nums[i] == random_num_element:
        equal.append(nums[i])
      else:
        greater.append(nums[i])

    if k <= len(less):
      return self.findKthSmallest(less, k)
    elif len(less) < k <= len(less) + len(equal):
      return equal[0]
    else:
      return self.findKthSmallest(greater, k - len(less) - len(equal))

  def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l = len(nums) - k + 1
    return self.findKthSmallest(nums, l)

if __name__ == '__main__':
  sol = Solution()
  # nums, k = [3,2,1,5,6,4], 2
  # nums, k = [2, 1], 2
  # nums, k = [3,2,3,1,2,4,5,5,6], 4
  nums, k = [3,2,3,1,2,4,5,5,6], 9
  print(sol.findKthLargest(nums, k))