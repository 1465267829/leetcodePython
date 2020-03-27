# https://youtu.be/trjnr4VOfk8

class SelectionSort:
  def sort(self, nums):
    if not nums: return []
    # len(nums)-1 is an optimization as it saves 1 swap
    for i in range(len(nums)-1):
      min_index = i
      for j in range(i+1, len(nums)):
        if nums[j] < nums[min_index]: min_index = j
      nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums

if __name__ == '__main__':
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  # nums = [9, 8, 7, 6, 9, 4, 3, 2, 1, 0]
  # nums = [0]
  sol = SelectionSort()
  print(sol.sort(nums))