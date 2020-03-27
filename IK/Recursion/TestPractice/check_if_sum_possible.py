def helper(nums, nums_index, slate, target):
  # backtrack
  if target == 0 and len(slate): return True

  #base
  if nums_index == len(nums): return False

  #recurse
  # exclude
  ret_exclude = helper(nums, nums_index + 1, slate, target)
  # include
  slate.append(nums[nums_index])
  ret_include = helper(nums, nums_index + 1, slate, target-nums[nums_index])
  slate.pop()
  if ret_exclude or ret_include: return True
  return False


def check_if_sum_possible(arr, k):
  return helper(arr, 0, [], k)


if __name__ == '__main__':
  arr, k = [2,4,8], 5
  # arr, k = [1], 0
  # arr, k = [0], 0
  print(check_if_sum_possible(arr, k))