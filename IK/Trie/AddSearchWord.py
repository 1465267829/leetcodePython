"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class TrieNode:
  def __init__(self):
      self.children = {}
      self.is_word = False


class WordDictionary:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()
    self.result = None

  def addWord(self, word: str) -> None:
    """
    Adds word to a trie
    """
    current = self.root
    for letter in word:
      if letter in current.children:
        current = current.children[letter]
      else:
        current.children[letter] = TrieNode()
        current = current.children[letter]
    current.is_word = True

  def helper(self, root, word):
    if not word:
      if root.is_word:
        self.result = True
      return
    # Extract the 1st char from the word
    current_char = word[0]
    if current_char == '.':
      # current_char is . that means we DFS all the children
      # trying to find a matching word
      for current in root.children.values():
        self.helper(current, word[1:])
    else:
      # Try to find the exact character
      # if not we can backtrack and return
      if current_char in root.children:
        current = root.children[current_char]
        self.helper(current, word[1:])
      else:
        return

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the data structure.
    A word could contain the dot character '.' to represent any one letter.
    """
    self.result = False
    self.helper(self.root, word)
    return self.result


if __name__ == '__main__':
  word_dict = WordDictionary()
  # word_dict.addWord('bad')
  # word_dict.addWord('mad')
  # # print(word_dict.search('pad'))
  # # print(word_dict.search('mad'))
  # print(word_dict.search('.ad'))
  # print(word_dict.search('.ax'))
  foo = ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search", "search", "search", "search", "search"]
  bar = [[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]

  word_dict.addWord('at')
  word_dict.addWord('and')
  word_dict.addWord('an')
  word_dict.addWord('add')
  print(word_dict.search('a'))

