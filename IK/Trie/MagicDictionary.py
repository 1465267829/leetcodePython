"""
https://leetcode.com/problems/implement-magic-dictionary/

676. Implement Magic Dictionary

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another
character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after
the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted
across multiple test cases. Please see here for more details.

"""
from typing import *


class MagicDictionary:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.md = {}

  def buildDict(self, dict: List[str]) -> None:
    """
    Build a dictionary through a list of words
    """
    for word in dict:
      current = self.md
      for letter in word:
        current = current.setdefault(letter, {})
      # presence of $ key in the children indicates
      # we are at the end of the word
      current.setdefault('$', '')

  def search(self, word: str) -> bool:
    def neighbor_search(parent, reg_index, current_word_index):
      if current_word_index == len(word):
        return '$' in parent

      current_letter = word[current_word_index]
      if reg_index == current_word_index:
        # "if reg_index == current_word_index: indicates"
        # that the current character at index current_word_index needs to
        # be treated as . in regexp
        # in this case explore all the valid neighbors
        # valid neighbors are
        # surrounding character in the grid
        # and not end of the word
        potential_neighbors = [v for k, v in parent.items() if word[reg_index] != k and k != '$']
        if not potential_neighbors:
          return False
        for current in potential_neighbors:
          return neighbor_search(current, reg_index, current_word_index+1)
      else:
        # treat this character at face value and search for next character
        # in the current trie subtree
        current = parent.get(current_letter, False)
        return False if not current else neighbor_search(current, reg_index, current_word_index+1)

    matched = False
    for reg_index in range(len(word)):
      # idea is to treat each character in the word as .
      # for regular expression and see if we have a word
      # in trie that matches
      if neighbor_search(self.md, reg_index, 0):
        matched = True
    return matched


if __name__ == '__main__':
  md = MagicDictionary()
  # dict = ["hello", "leetcode"]
  dict = ["hello","hallo","leetcode"]
  md.buildDict(dict)
  ip = ['hello', 'hhllo', 'hell', 'leetcoded']
  ip = ['helloaaaa']
  for i in ip: print(md.search(i))
  '''
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
  '''
