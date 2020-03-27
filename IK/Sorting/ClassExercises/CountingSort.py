# https://youtu.be/WcuyNvz4j5w

from queue import Queue

class CountingSort:
  def sort(self, nums):
    # make a bucket of size max range of inputs
    # MAX_RANGE = 0..10, using index as bucket id
    buckets = [Queue() for _ in range(0, 11)]

    for num in nums: buckets[num].put(num)

    result = []
    for _, queue in enumerate(buckets):
      while not queue.empty(): result.append(queue.get())
    return result

if __name__ == '__main__':
  nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  nums = [9, 8, 7, 6, 9, 4, 3, 2, 0, 0]
  nums = [0]
  nums = [-1, -1]
  nums = []
  nums = [-1, -1, -1]
  nums = [9, 9, 2, 4, 9, 9, 1, 0]
  sol = CountingSort()
  print(sol.sort(nums))
