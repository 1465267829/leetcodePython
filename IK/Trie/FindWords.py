"""
https://leetcode.com/problems/word-search-ii/

212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

from typing import *


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def build_trie():
      """
      Here trie node is a dict with keys being the letters that form the children
      of current node and value being a dict which will contains children of node denoted by
      the key.
      If a node happens to be the last letter of a word then it would have a special child key
      '$' with value being the entire word that terminates at that node.
      The presence of $ as a key in the node denotes that it is the last letter of a word
      in the dictionary and the word that it is the last letter of the the value of such a child key
      for example:
      'abc' inserted in the trie would make it look like this

      {
        a : {
          b : {
            c : {
              $: 'abc'
            }
          }
        }
      }
      """
      for word in words:
        node = trie
        for letter in word:
          # here letter can be present in the current node as it's
          # child or absent
          # case 1:
          # if the current letter is present as child of
          # the current node then current node becomes such a child node
          # case 2:
          # if the current letter is absent as a child of
          # the current node then current node adds letter as child key and value being {}
          # the current node then current node becomes such a newly created child node
          if letter not in node: node[letter] = {}
          node = node[letter]
        node[WORD_KEY] = word

    def explore(row, col, parent):
      # we note the current letter so that we can restore the board
      # after the recursion
      letter = board[row][col]

      # here parent is the node that was last visited in the trie tree
      current_node = parent[letter]

      # if current_node has a child with key WORD_KEY then current_node must
      # be a letter marking a end of word in the dict
      # if so, then remove such a word and append to matched_words
      # we remove this word to avoid accounting for it twice
      word_match = current_node.pop(WORD_KEY, False)
      if word_match:
        matched_words.append(word_match)

      # mark board[row][col] as # to avoid circular references
      board[row][col] = '#'
      offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      for row_offset, col_offset in offsets:
        new_row, new_col = row + row_offset, col + col_offset
        # if new_row, new_col are on board
        # and if new_row, new_col have not been visited as part of this exploration
        # and if letter in the new cell is a child of current_node then continue exploring
        # else
        # backtrack
        if 0 <= new_row < row_num and 0 <= new_col < col_num and board[new_row][new_col] != '#' and board[new_row][new_col] in current_node:
          explore(new_row, new_col, current_node)
      # restore the cell after exploration
      board[row][col] = letter

    trie = {}
    WORD_KEY = '$'
    build_trie()
    matched_words = []
    row_num = len(board)
    col_num = len(board[0])
    for row in range(row_num):
      for col in range(col_num):
        if board[row][col] in trie:
          # the current letter is in trie then explore
          # else
          # backtrack
          explore(row, col, trie)
    return matched_words


if __name__ == '__main__':
  sol = Solution()
  board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
  ]
  # board = [
  #   ['o', 'a'],
  #   ['e', 't']
  # ]
  words = ["oath", "pea", "eat", "rain"]
  print(sol.findWords(board, words))
