"""
https://leetcode.com/problems/word-break-ii/

140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution:
  def wordBreak(self, s, wordDict):
    words = set(wordDict)
    splittable_at_index = [False] * (1+len(s))
    splittable_at_index[0] = True

    for i in range(0, len(s)):
      for j in range(i, -1, -1):
        if s[j:i+1] in words and splittable_at_index[j]:
          splittable_at_index[i+1] = True
    return splittable_at_index[-1]


if __name__ == '__main__':
  sol = Solution()
  s, wordDict = 'catsanddog', ["cat", "cats", "and", "sand", "dog"]
  # s, wordDict = 'pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]
  # s, wordDict = 'catsandog', ["cats", "dog", "sand", "and", "cat"]
  print(sol.wordBreak(s, wordDict))
