"""
https://leetcode.com/problems/replace-words/

648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000

"""
from typing import *


class Solution:
  def replaceWords(self, dict: List[str], sentence: str) -> str:
    def triefy():
      for word in dict:
        current = trie
        for letter in word:
          if letter not in current: current[letter] = {}
          current = current[letter]
        current['$'] = word

    def find_replacement(word):
      current = trie
      for letter in word:
        if letter in current:
          prefix = current.get('$', None)
          if prefix: return prefix
          current = current[letter]
        else:
          break
      replacement = current.get('$', word)
      return replacement

    trie = {}
    triefy()
    sentence_words = sentence.split(' ')
    for word_index in range(len(sentence_words)):
      sentence_words[word_index] = find_replacement(sentence_words[word_index])
    return ' '.join(sentence_words)


if __name__ == '__main__':
  sol = Solution()
  dict = ["cat", "bat", "rat"]
  sentence = "the cattle was rattled by the battery"
  dict = ["a", "aa", "aaa", "aaaa"]
  sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
  print(sol.replaceWords(dict, sentence))
