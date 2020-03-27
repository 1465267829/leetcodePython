"""
https://leetcode.com/problems/palindrome-pairs/

336. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""

from typing import *

WORD_END_INDEX = '$'
PALINDROME_SUFFIXES = '#'


class Solution:
  def isPalindrome(self, word, left, right):
    while left < right:
      if word[left] != word[right]: return False
      left += 1
      right -= 1
    return True

  def createSuffixTrie(self, words):
    # create a trie from reverses of all the words
    suffix_trie = {}
    for word_index, word in enumerate(words):
      # reverse the word to insert in trie
      reversed_word = word[::-1]
      current = suffix_trie
      for letter_index, letter in enumerate(reversed_word):
        # if the letter is not in current subtree then create
        # the letter node key and assign the empty {} for children's to come
        if letter not in current: current[letter] = {}
        # if the remainder of the word starting at letter_index till end of word
        # is a palindrome then insert the index of such a word at the current
        # letter node in the trie. This avoids us doing BFS and find if the rest of the word is
        # a palindrome or not for case 2
        # better explanation is here:
        # https://leetcode.com/problems/palindrome-pairs/solution/
        # When we insert a word, we can start by determining all of its palindrome prefixes.
        # Now, on each node we'll attach a list of all words that have a palindrome remaining on them.
        # For the example you worked through, this is the words you identified in part 2.
        if self.isPalindrome(reversed_word, letter_index, len(reversed_word)-1):
          if PALINDROME_SUFFIXES not in current: current[PALINDROME_SUFFIXES] = []
          current[PALINDROME_SUFFIXES].append(word_index)
        # mode down the trie
        current = current[letter]
      # set the last word index
      current[WORD_END_INDEX] = word_index
    return suffix_trie

  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    suffix_trie = self.createSuffixTrie(words)
    result = []
    for word_index, word in enumerate(words):
      current_trie_node = suffix_trie
      for letter_index, letter in enumerate(word):
        if WORD_END_INDEX in current_trie_node:
          # case 3:
          # here we are still traversing the current word to find the palindrome
          # pair and saw a word ending at current_trie_node. This means current word in longer
          # and the word that ended at current_trie_node is shorter.
          # If the remainder of current word is a palindrome then we found a pair
          # Pair being the current word index and the index of word that ended at current_trie_node.
          if self.isPalindrome(word, letter_index, len(word)-1):
            result.append([word_index, current_trie_node[WORD_END_INDEX]])
        if letter not in current_trie_node:
          break
        current_trie_node = current_trie_node[letter]
      else:
        # Here we have considered all the letters of the current word
        # Here either we can find word that is exactly mirror of current word
        # or 2nd word is longer than the current word.

        # If we find that current_trie_node here points to end of a word then we have a mirror word.
        # We have inserted reverse of the words in suffix_trie, so to avoid accounting for the word itself
        # inserted in current_trie_node we check if current_trie_node[WORD_END_INDEX] is not word_index
        # If they are not equal then we found another pair.

        # case 1:
        # if we find current_trie_node point to end of the word then we have a mirror word.
        # if mirror word index is not equal to current word index then we truly have a exact
        # mirror word in the words.
        # Add such an index to result
        if WORD_END_INDEX in current_trie_node and current_trie_node[WORD_END_INDEX] != word_index:
          result.append([word_index, current_trie_node[WORD_END_INDEX]])

        # case 2:
        # here we have current word is shorter
        # we see if current_trie_node is in path of any palndrom suffixes.
        # if so, add each such index to result.
        if PALINDROME_SUFFIXES in current_trie_node:
          for pallindrom_suffix_index in current_trie_node[PALINDROME_SUFFIXES]:
            result.append([word_index, pallindrom_suffix_index])
    return result


if __name__ == '__main__':
  sol = Solution()
  # words = ["abcd", "dcba", "lls", "s", "sssll"]
  words = ["bat","tab","cat"]
  # words = ["A", "B", "BAN", "BANANA", "BAT", "LOLCAT", "MANA", "NAB", "NANA", "NOON", "ON", "TA", "TAC"]
  # words = ["A", "B", "BAN", "BANANA", "BAT", "LOLCAT", "BIGCAT", "LILCAT", "OLCAT", "MACAT", "ACAT", "MANA", "NAB", "NANA", "NOON", "ON", "TA", "TAC"]
  print(sol.palindromePairs(words))
