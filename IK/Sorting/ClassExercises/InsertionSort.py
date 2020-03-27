# https://youtu.be/FK8OJGcsa2I

class InsertionSort:
  def sort_recursive_shift_right(self, nums):

    ############################################
    ## Helper function starts
    ############################################
    def sort_recursive_shift_right_helper(nums, i):
      if i <= 0: return
      sort_recursive_shift_right_helper(nums, i - 1)
      temp = nums[i]
      j = i - 1

      # Find the insertion place
      while j >= 0 and nums[j] > nums[i]:
        j -= 1

      k = i - 1
      while j < k <= i:
        # Right shift
        nums[k + 1] = nums[k]
        k -= 1
      nums[k + 1] = temp
      return nums
      ############################################
      ## Helper function ends
      ############################################

    sort_recursive_shift_right_helper(nums, len(nums) - 1)
    return nums

  def sort_recursive_bubble(self, nums):

    ############################################
    ## Helper function starts
    ############################################
    def sort_recursive_bubble_helper(nums, i):
      if i <= 0: return
      sort_recursive_bubble_helper(nums, i - 1)
      j = i - 1
      while j >= 0 and nums[j] > nums[j + 1]:
        nums[j + 1], nums[j] = nums[j], nums[j + 1]
        j -= 1
      return nums
    ############################################
    #E Helper function ends
    ############################################

    sort_recursive_bubble_helper(nums, len(nums) - 1)
    return nums

  def sort_iterative_bubble(self, nums):
    for i in range(1, len(nums)):
      j = i - 1
      while j >= 0 and nums[j] > nums[j + 1]:
        # bubble method
        nums[j + 1], nums[j] = nums[j], nums[j + 1]
        j -= 1
    return nums

  def sort_iterative_right_shift(self, nums):
    for i in range(1, len(nums)):
      temp = nums[i]
      j = i - 1

      # Find the insertion place
      while j >= 0 and nums[j] > nums[i]:
        j -= 1

      # Right shift
      k = i - 1
      while j < k <= i:
        nums[k + 1] = nums[k]
        k -= 1
      nums[k + 1] = temp
    return nums

if __name__ == '__main__':
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  # nums = [9, 8, 7, 6, 9, 4, 3, 2, 1, 0]
  # nums = [0]
  # nums = [-1, -1]
  nums = [1, 2, 4, 0]
  sol = InsertionSort()
  print(sol.sort_recursive_bubble(nums))
  print(sol.sort_recursive_shift_right(nums))
  print(sol.sort_iterative_bubble(nums))
  print(sol.sort_iterative_right_shift(nums))