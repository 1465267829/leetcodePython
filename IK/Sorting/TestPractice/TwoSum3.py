"""
https://leetcode.com/problems/two-sum-iii-data-structure-design/

170. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""
class TwoSum:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.nums = {}

  def add(self, number: int) -> None:
    """
    Add the number to an internal data structure..
    """
    if number not in self.nums: self.nums[number] = 0
    self.nums[number] += 1

  def find(self, value: int) -> bool:
    """
    Find if there exists any pair of numbers which sum is equal to the value.
    """
    for i in self.nums.keys():
      j = value - i
      if i == j and self.nums.get(i) > 1 or i != j and self.nums.get(j, 0) > 0:
        return True
    return False

if __name__ == "__main__":
  sol = TwoSum()
  # for i in [1, 3, 5]: sol.add(i)
  # for i in [4, 7]: print(sol.find(i))

  for i in [3,1,2]: sol.add(i)
  for i in [3,6]: print(sol.find(i))