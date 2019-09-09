"""
239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 0 or k == 0: return []
    if k == 1: return nums
    deq = []
    result = []

    for i, val in enumerate(nums):
      # if the 1st element of deq is an index which is out of current window
      # pop that elementr from deq
      if deq and deq[0] == i - k:
        deq.pop(0)

      # while deq exists and last element of deq point to an index of nums which
      # has an element less than val, keep poping the last index in deq
      while deq and val > nums[deq[-1]]:
        deq.pop()

      # append current index
      deq.append(i)

      # add to the result in the nums correspoing to 0the element as that is
      # gaurtenned to be the max of nums in the current window
      if i >= k - 1: result.append(nums[deq[0]])

    return result

if __name__ == '__main__':
  sol = Solution()
  print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))