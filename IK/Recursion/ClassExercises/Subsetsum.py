class Solution:
  def helper(self, nums, nums_index, slate, slate_sum, result, target):
    if slate_sum > target:
      return
    if slate_sum == target:
      result.append(slate[:])
      return
    if nums_index == len(nums):
      return
    # exclude
    self.helper(nums, nums_index+1, slate, slate_sum, result, target)
    # include
    slate.append(nums[nums_index])
    slate_sum += nums[nums_index]
    self.helper(nums, nums_index+1, slate, slate_sum, result, target)
    slate_sum -= nums[nums_index]
    slate.pop()
    return

  def subset_sum(self, nums, k):
    nums_index, slate, slate_sum, result, target = 0, [], 0, [], k
    self.helper(nums, nums_index, slate, slate_sum, result, target)
    return result


if __name__ == '__main__':
  sol = Solution()
  nums, k = [2,3,6,7], 7
  nums, k = [2,5,2,1,2], 5
  print(sol.subset_sum(nums, k ))