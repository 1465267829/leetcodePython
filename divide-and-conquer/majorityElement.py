'''
169. Majority Element
https://leetcode.com/problems/majority-element/
'''
class Solution(object):
  def majorityElement0(self, nums):
    """
    Divide and Conquer with sublists
    """
    if len(nums) == 1:
      return nums[0]
    left_list = nums[:len(nums) // 2]
    right_list = nums[len(nums) // 2:]
    left_majority = self.majorityElement0(left_list)
    right_majority = self.majorityElement0(right_list)
    if left_majority == right_majority: return left_majority
    left_majority_count = 0
    right_majority_count = 0
    for e in nums:
      if e == left_majority: left_majority_count += 1
      if e == right_majority: right_majority_count += 1
    return right_majority if left_majority_count < right_majority_count else left_majority

  def majorityElement1(self, nums):
    """
    Using a dict
    """
    nums_map = {}
    for e in nums:
      if not e in nums_map: nums_map[e] = 0
      nums_map[e] += 1

    max_value = 0
    max_freq = 0

    for value, freq in nums_map.iteritems():
      if freq >= max_freq: max_value, max_freq = value, freq

    return max_value

  def majorityElement2(self, nums):
    """
    Divide and Conquer with indices
    """
    def majorityElement2helper(start, end):
      if start == end: return nums[start]
      mid = start + (end - start) // 2
      left_majority = majorityElement2helper(start, mid)
      right_majority = majorityElement2helper(mid + 1, end)
      if left_majority == right_majority: return left_majority

      left_majority_count = 0
      right_majority_count = 0
      for i in range(start, end + 1):
        if nums[i] == left_majority: left_majority_count += 1
        if nums[i] == right_majority: right_majority_count += 1

      return left_majority if left_majority_count > right_majority_count else right_majority

    return majorityElement2helper(0, len(nums) - 1)

  def majorityElement3(self, nums):
    # Boyer-Moore Voting Algorithm
    majority_num = nums[0]
    majority_freq = 1

    for i in range(1, len(nums)):
      if nums[i] == majority_num:
        majority_freq += 1
      else:
        if majority_freq == 0:
          majority_freq = 1
          majority_num = nums[i]
        else:
          majority_freq -= 1
    return majority_num

if __name__ == '__main__':
  sol = Solution()
  print sol.majorityElement0([3,3,4])
  print sol.majorityElement1([3,3,4])
  print sol.majorityElement2([3,3,4])
  print sol.majorityElement3([3,3,4])
