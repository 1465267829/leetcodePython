"""
Partition in place nums such that all the elements
equal to k are between element less than k on left and more than k
on right
k is guaranteed to be in nums
"""


class DutchNationFlag:
  def partition(self, nums, k):
    less, equal, more = -1, 0, len(nums)
    while equal < more:
      if nums[equal] < k:
        less += 1
        nums[less], nums[equal] = nums[equal], nums[less]
        equal += 1
      elif nums[equal] > k:
        more -= 1
        nums[more], nums[equal] = nums[equal], nums[more]
      else:
        equal += 1
    print(nums)
    print(less, equal, more)
    print(nums[:less+1])
    print(nums[less+1:equal])
    print(nums[equal+1:len(nums)])
    # less is at index which has last element less than k
    # more is at index which has first element more than k
    return nums


if __name__ == '__main__':
  # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 5, 5, 5, 5]
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  sol = DutchNationFlag()
  print(sol.partition(nums, 5))