"""
https://leetcode.com/problems/word-ladder/

127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import *
from string import ascii_lowercase


class Solution:
  def __init__(self):
    # we use wordlist to keep the words
    # in from dict
    # We remove the word wordList once the word
    # is used as a transformation
    # wordList is being used as visited array
    # from class
    self.wordList = set()

  def discover_neighbors(self, word):
    """
    # discover_neighbors has following constraints here:
    # 1. Discovered words should be one transformation distance from word.
    # 2. Transformation is defined in the problem as change one char from
    #    given word at a time
    #    For example:
    #    For word 'hit'; '*it', 'h*t', 'hi*' are family of valid transformations,
    #    where each * is [a...z]
    # 3. Once all the neighboring words are discovered, they have to be
    #    filtered based on availability in the wordList
    # 4. Once the neighbor is discovered and filtered, the word should be
    #    removed from wordList for avoiding cycles
    """
    neighbors = []
    for i in range(len(word)):
      temp = list(word)
      for alpha in ascii_lowercase:
        temp[i] = alpha
        if tuple(temp) in self.wordList:
          neighbors.append(tuple(temp))
          self.wordList.remove(tuple(temp))
    return neighbors

  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    # Here graph generation is in the fly
    # Think of this problem as those martix graph problems
    # here discover_neighbors plays crucial part of
    # discovering the neighbors based on constraints
    """
    for word in wordList:
      self.wordList.add(tuple([word[i] for i in range(len(word))]))

    bword = tuple([beginWord[i] for i in range(len(beginWord))])
    eword = tuple([endWord[i] for i in range(len(endWord))])

    # Start BFS and track the level as num_transform
    # num_transform here tells us how many transformations
    # have been applied to beginWord so far
    num_transform = 0
    q = [bword]
    while q:
      num_transform += 1
      for _ in range(len(q)):
        curr = q.pop(0)
        if curr == eword:
          return num_transform
        for n in self.discover_neighbors(curr):
          q.append(n)
      pass # while
    return 0


if __name__ == '__main__':
  sol = Solution()
  # beginWord, endWord, wordList = 'hit', 'cog', ["hot","dot","dog","lot","log","cog"]
  # beginWord, endWord, wordList = 'hit', 'cog', ["hot","dot","dog","lot","log"]
  beginWord, endWord, wordList = 'hot', 'dog', ["hot","dog"]
  print(sol.ladderLength(beginWord, endWord, wordList))
