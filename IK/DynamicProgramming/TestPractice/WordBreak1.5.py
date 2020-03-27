"""
This WordBreak1.5 problem is similar to wordBreak as this problem builds on to wordBreak1 adding the number of
possible spilts to be reported.

Here the formal question from IKWeb
Word Break Count



Problem Statement:



You are given a dictionary set dictionary that contains dictionaryCount distinct words and another string txt. Your task is to count the possible number of the word-breaks of the txt string in such a way that all the word occur in a continuous manner in the original txt string and all these words exist in our dictionary set dictionary.



In short, you have to split the string txt using ‘ ‘(single white space delimiter) in such a way that every segment (word) exists in our dictionary.



The same word from the dictionary can be used multiple times when splitting the given string.



Example: Suppose our Dictionary is {“to”, “do”, “todo”}

and txt is “totodo” then it can also be segmented as

“to to do”. Here the word “to” from the dictionary is being used twice.



Input/Output Format For The Function:



Input Format:



The first parameter of the function that is to be implemented is an integer dictionaryCount denoting, the number of words in our dictionary. The second parameter is an array of strings dictionary, denoting the list of words in our dictionary and the last parameter is a string txt, denoting the text string that is to be segmented.



Output Format:



Return an integer denoting all different possible word-break arrangements for the txt string. This integer could be large so output it modulo 10^9 + 7.



Input/Output Format For The Custom Input:



Input Format:



The first line of the input contains one single integer denoting dictionaryCount, the number of words in our dictionary.

Next dictionaryCount lines contain strings denoting words in our dictionary. Next line contains one single string denoting the txt string.

If dictionaryCount = 2 , dictionary = [“hello” , “world”] and

txt = “helloworld” then custom input format will be:



2

hello

world

helloworld



Output Format:



Print one integer denoting all different possible word-break arrangements for the txt string.

For the above-provided custom input, output there is only one way to partition the txt string ( “hello world”), so the output will be:



1



Constraints:



1 <= dictionaryCount <= 200000
1 <= length(txt) <= 2000
1<= length of words in dictionary <= 100
All the characters in txt and words in dictionary are lower case English alphabets.


Sample Test Case:



7

kick

start

kickstart

is

awe

some

awesome

kickstartisawesome



Sample Output:



4



Explanation:



There are only 4 possible segmentations possible for the given txt and 4 % 1000000007 = 4. All four of which are mentioned below:



kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome


Consider first word-break arrangement: “kick start is awe some”

Here all the words: kick, start, is, awe and some exist in our dictionary and these words are continuous substrings of the txt string “kickstartisawesome”.



Similarly, other three word-breaks satisfy the same conditions and hence are valid word-breaks of the given string


"""
"""
https://leetcode.com/problems/word-break/

139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

from typing import *


# Brut Force
# class Solution:
#   def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     # empty string evaluates to True
#     if not s: return True
#
#     word_dict = set(wordDict)
#
#     for i in range(len(s)+1):
#       left_string = s[0:i]
#       right_string = s[i:len(s)]
#       if left_string in word_dict:
#         if self.wordBreak(right_string, wordDict):
#           return True
#     return False

# DP: Memoized
# class Solution:
#   """
#   # Recurrent equation is:
#   As described in
#   splittable(i) = True for i > n
#   splittable(i) = V(j=1 to j=n)[isword(0, j) AND splittable(j+1)] for i <= n
#   Book: Algorithms by Jeff Erickson Page 83
#
#   Simply stated
#   Given a string s, to determine if a string s is splittable;
#   1.  We loop through the string s with index from [0..len(s)], (both inclusive)
#       example:
#       for s = 'leetcode', we go
#       index=0 left = '' and right = 'leetcode'
#       index=1 left = 'l' and right = 'eetcode'
#       index=2 left = 'le' and right = 'etcode'
#       index=3 left = 'lee' and right = 'tcode'
#       index=4 left = 'leet' and right = 'code'
#       index=5 left = 'leetc' and right = 'ode'
#       index=6 left = 'leetco' and right = 'de'
#       index=7 left = 'leetcod' and right = 'e'
#       index=8 left = 'leetcode' and right = ''
#
#   2.  While we are at an index 'i' we conclude the following
#       IF the substring starting from index 0 to i-1 (both inclusive) [left in example above] is a word in dict
#       AND IF substring starting from i to len(s) (both inclusive) [right in example above] is splittable
#       then the entire string s is splittable at index into words that are found in the dict
#
#       ELSE
#       it is not
#
#   3. Since splittable will be called on duplicate substrings we can do a top dowm memoization.
#      In the last example below, memoized data structure, for example; is hit 378 times and memo has a key length of 49
#   """
#   def __init__(self):
#     self.s = None
#     self.words = None
#     self.memo = {}
#     self.memo_dup = []
#
#   def splittable(self, start):
#     if start in self.memo:
#       return self.memo[start]
#
#     for i in range(start, len(self.s)+1):
#       if self.s[start:i] in self.words and self.splittable(i):
#           self.memo[start] = True
#           self.memo_dup.append(start)
#           return self.memo[start]
#     self.memo_dup.append(start)
#     self.memo[start] = False
#     return self.memo[start]
#
#   def wordBreak(self, s, wordDict):
#     self.s = s
#     # Convert wordDict to a hashset for O(1) lookups
#     self.words = set(wordDict)
#     self.memo[len(self.s)] = True
#     ret = self.splittable(0)
#     return ret

# DP: Bottom up
class Solution:
  """
  Recurrent equation is:
  f(n) = True if s[0..n-1] can be split into one or more dict words

  is defined in terms of subproblems as
  f(i) = if any substring rooted at i is splittable
  f(i) = OR over all j (The last j characters are in the dict and f(i-j) is True)


  For example s, wordDict = 'leetcode', ['leet', 'code']
  Following is how it looks

  splittable_at_index       : T F F F T F F F T
  splittable_at_index index : 0 1 2 3 4 5 6 7 8
  s                         : l e e t c o d e
  s index                   : 0 1 2 3 4 5 6 7

  Idea is the following:
  1.  Iterate the entire string 's' char by char from left to right

  2.  a.  While are at an index i of the string 's' we generate all the substrings/words
          rooted at index i and growing leftward.
          All these words could be potentially the last word after the split.
          For example:
          For string 'leetcode', where i = 7
          We generate the following substrings
          j = 7 'e'
          j = 6 'de'
          j = 5 'ode'
          j = 4 'code'
          j = 3 'tcode'
          j = 2 'etcode'
          j = 1 'eetcode'
          j = 0 'leetcode'
    b. For each such generated substring s[j:i+1] we ask the question:

      Is the generated substring s[j:i+1] a valid word in dict ?
      AND
      Is the substring s[0, j] is splittable ?

      If both the above questions are true, then we conclude that substring s[0:i+1] can be spilt such that all
      the words after spilt are in dict.

      If any one or more answer(s) to above question is/are False., then we conclude that substring s[0:i+1] is not
      splittable.

  3.  At the end of iteration over string s we will be able to conclude if we can split the word or not.
      Remember there may be 0 or more ways to split the input string. If answer is 0 then we return False else True

  4.  Here overlapping subproblems are "Is the substring s[0, j] is splittable ?"

  5.  Answer of the above question is maintained in a 1D table called 'splittable_at_index'.
      Value at index 'i' of 'splittable_at_index' represents, if substring of length i of string 's' is splittable.
      For example:
      splittable_at_index[0] as True means, substring '' (empty string, length 0) of string 's' is splittable [Base Case]
      splittable_at_index[1] as False means, substring 'l' (length 1) of string 's' is not splittable
      splittable_at_index[2] as False means, substring 'le' (length 2) of string 's' is not splittable
      splittable_at_index[3] as False means, substring 'lee' (length 3) of string 's' is not splittable
      splittable_at_index[4] as True means, substring 'leet' (length 4) of string 's' is splittable
      splittable_at_index[5] as False means, substring 'leetc' (length 5) of string 's' is not splittable
      splittable_at_index[6] as False means, substring 'leetco' (length 6) of string 's' is not splittable
      splittable_at_index[7] as False means, substring 'leetcod' (length 7) of string 's' is not splittable
      splittable_at_index[8] as True means, substring 'leetcode' (length 8) of string 's' is splittable

  6.  If we look carefully, while we are at index i of string 's', we are solving the subproblem for which answer
      needs to go in i+1 th location in splittable_at_index.
      For example:
      i=0 Gets us 'l', in example <s, wordDict = 'leetcode', ['leet', 'code']>
      Answer to question "Is the substring s[0, j] is splittable ?" which is "Is the substring 'l' is splittable ?"
      is stored in index 1 of splittable_at_index.

  6.  If we look carefully, while we are at index i of string 's', we are solving the subproblem for which answer
      needs to go in i+1 th location in splittable_at_index, we need the value of answer in jth location of splittable_at_index
  """
  def wordBreak(self, s, wordDict):
    words = set(wordDict)
    splittable_at_index = [0] * (1+len(s))
    splittable_at_index[0] = 1

    for i in range(0, len(s)):
      for j in range(i, -1, -1):
        if s[j:i+1] in words and splittable_at_index[j]:
          splittable_at_index[i+1] += splittable_at_index[j]
    return splittable_at_index[-1] % 1000000007


if __name__ == '__main__':
  sol = Solution()
  s, wordDict = 'kickstartisawesome', ['kick', 'start', 'kickstart', 'is', 'awe', 'some', 'awesome']
  # s, wordDict = 'leetcode', ['leet', 'code']
  # s, wordDict = 'leet', ['leet', 'code']
  # s, wordDict = 'applepenapple', ["apple", "pen"]
  # s, wordDict = 'catsandog', ["cats", "dog", "sand", "and", "cat"]
  # s, wordDict = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
  print(sol.wordBreak(s, wordDict))