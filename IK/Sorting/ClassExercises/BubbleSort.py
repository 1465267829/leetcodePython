# https://youtu.be/_QEG3xvDntQ


class BubbleSort:
  def sort(self, nums):
    if not nums: return []
    for i in range(len(nums)):
      for j in range(len(nums)-1, i, -1):
        if nums[j] < nums[j-1]:
          nums[j], nums[j-1] = nums[j-1], nums[j]
      pass
    return nums


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # nums = [9, 8, 7, 6, 9, 4, 3, 2, 1, 0]
    # nums = [0]
    sol = BubbleSort()
    print(sol.sort(nums))