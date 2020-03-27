"""
https://leetcode.com/problems/map-sum-pairs/

677. Map Sum Pairs

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer
represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs'
value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum:

  def __init__(self):
    self.trie = {}
    self.END_MARKER = '$'

  def insert(self, key: str, val: int) -> None:
    current = self.trie
    for letter in key:
      if letter not in current:
        current[letter] = {}
      current = current[letter]
    current[self.END_MARKER] = val

  def sum(self, prefix: str) -> int:
    def find_prefix():
      current = self.trie
      for letter in prefix:
        current = current.get(letter, None)
        if not current: return current
      return current

    def find_sum(current):
      for key, value in current.items():
        if key == self.END_MARKER:
          # current mark's end of a word. add value
          result[0] += value
          continue
        find_sum(value)

    result = [0]
    prefix_node = find_prefix()
    if not prefix_node: return result[0]
    find_sum(prefix_node)
    return result[0]


if __name__ == '__main__':
  obj = MapSum()
  obj.insert('apple', 3)
  print(obj.sum('ap'))
  obj.insert('app', 2)
  print(obj.sum('ap'))
  obj.insert('appbe', 7)
  print(obj.sum('ap'))
