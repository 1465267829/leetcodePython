'''
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#LCS_function_defined
http://www.cs.cmu.edu/afs/cs/academic/class/15451-s15/LectureNotes/lecture04.pdf
https://leetcode.com/problems/longest-common-subsequence/submissions/
1143. Longest Common Subsequence
'''
import random
class Solution(object):

  def lcs_recursive_end(self, text1, text2, end_text1, end_text2):
    if end_text1 == -1 or end_text2 == -1: return 0
    if text1[end_text1] == text2[end_text2]:
      return 1 + self.lcs_recursive_end(text1, text2, end_text1 - 1, end_text2 - 1)
    else:
      return max(
        self.lcs_recursive_end(text1, text2, end_text1, end_text2 - 1),
        self.lcs_recursive_end(text1, text2, end_text1 - 1, end_text2)
      )

  def lcs_recursive_start(self, text1, text2, start_text1, start_text2):
    if start_text1 == len(text1) or start_text2 == len(text2): return 0
    if text1[start_text1] == text2[start_text2]:
      return 1 + self.lcs_recursive_start(text1, text2, start_text1 + 1, start_text2 + 1)
    else:
      return max(
        self.lcs_recursive_start(text1, text2, start_text1, start_text2 + 1),
        self.lcs_recursive_start(text1, text2, start_text1 + 1, start_text2)
      )

  def lcs_helper_start(self, text1, text2, start_text1, start_text2, memo):
    if start_text1 == len(text1) or start_text2 == len(text2): return 0
    if memo[start_text1][start_text2]:
      return memo[start_text1][start_text2]

    if text1[start_text1] == text2[start_text2]:
      memo[start_text1][start_text2] = 1 + self.lcs_helper_start(text1, text2, start_text1 + 1, start_text2 + 1, memo)
    else:
      memo[start_text1][start_text2] = max(self.lcs_helper_start(text1, text2, start_text1, start_text2 + 1, memo),
                                           self.lcs_helper_start(text1, text2, start_text1 + 1, start_text2, memo))
    return memo[start_text1][start_text2]

  def lcs_start(self, text1, text2):
    # top-down Dynamic Programming ??
    memo = [[None] * len(text2) for i in xrange(len(text1))]
    return self.lcs_helper_start(text1, text2, 0, 0, memo)

  def backtrack_lcs_end(self, text1, text2, memo):
    i = len(memo) - 1
    j = len(memo[0]) - 1
    lcs = ''
    while i > -1 and j > -1:
      if text1[i] == text2[j]:
        lcs = text1[i] + lcs
        i -= 1
        j -= 1
      else:
        if memo[i][j-1] > memo[i-1][j]:
          j -= 1
        else:
          i -= 1
    return lcs

  def lcs_helper_end(self, text1, text2, end_text1, end_text2, memo):
    if end_text1 == -1 or end_text2 == -1: return 0
    if memo[end_text1][end_text2]: return memo[end_text1][end_text2]
    if text1[end_text1] == text2[end_text2]:
      memo[end_text1][end_text2] = 1 + self.lcs_helper_end(text1, text2, end_text1 - 1, end_text2 - 1, memo)
    else:
      memo[end_text1][end_text2] = max(self.lcs_helper_end(text1, text2, end_text1, end_text2 - 1, memo),
                                       self.lcs_helper_end(text1, text2, end_text1 - 1, end_text2, memo))
    return memo[end_text1][end_text2]

  def lcs_end(self, text1, text2):
    # top-down Dynamic Programming ??
    memo = [[None] * len(text2) for i in xrange(len(text1))]
    lcs_length = self.lcs_helper_end(text1, text2, len(text1) - 1, len(text2) - 1, memo)
    lcs = self.backtrack_lcs_end(text1, text2, memo)
    return lcs

  def generate_memo(self, text1, text2):
    memo = []
    for i in xrange(len(text1) + 1):
      if i == 0:
        memo.append([0] * (len(text2) + 1))
      else:
        memo.append([0] + [None] * len(text2))
    return memo

  def backtrack_lcs(self, text1, text2, memo):
    i = len(memo) - 1
    j = len(memo[0]) - 1
    res = ''
    while i > 0 and j > 0:
      # while row/column more than 0, keep going
      if text1[i - 1] == text2[j - 1]:
        # if both chars are equal then go diagonally up left
        res = text1[i - 1] + res
        i -= 1
        j -= 1
      else:
        if memo[i][j-1] > memo[i-1][j]:
          # if top is greater than left, go top
          j -= 1
        elif memo[i-1][j] > memo[i][j-1]:
          # if left is greater than top, go left
          i -= 1
        else:
          # both are equal, can choose any, choose randomly
          choices = ['i','j']
          choice = random.choice(choices)
          if choice == 'i':
            i -= 1
          else:
            j -= 1
    return res

  def backtrack_lcs_recursive(self, text1, text2, text1_index, text2_index, memo):
    if text1_index == 0 or text2_index == 0:
      # if we one of the strings are consumed return empty
      return ''
    elif text1[text1_index-1] == text2[text2_index-1]:
      # if both chars are equal then go diagonally up left
      return self.backtrack_lcs_recursive(text1, text2, text1_index - 1, text2_index -1, memo) + text1[text1_index-1]
    else:
      if memo[text1_index][text2_index-1] > memo[text1_index-1][text2_index]:
        # if top is greater than left, go top
        return self.backtrack_lcs_recursive(text1, text2, text1_index, text2_index-1, memo)
      elif memo[text1_index - 1][text2_index] > memo[text1_index][text2_index - 1]:
        # if left is greater than top, go left
        return self.backtrack_lcs_recursive(text1, text2, text1_index-1, text2_index, memo)
      else:
        # both are equal, can choose any, choose randomly
        choices = [[text1_index, text2_index-1], [text1_index-1, text2_index]]
        choice = random.choice(choices)
        return self.backtrack_lcs_recursive(text1, text2, choice[0], choice[1], memo)

  def backtrack_lcs_recursive_all(self, text1, text2, text1_index, text2_index, memo):
    if text1_index == 0 or text2_index == 0:
      return set([''])
    elif text1[text1_index-1] == text2[text2_index-1]:
      return set([lcs + text1[text1_index-1] for lcs in self.backtrack_lcs_recursive_all(text1, text2, text1_index - 1, text2_index -1, memo)])
    else:
      lcs_set = set()
      if memo[text1_index][text2_index-1] > memo[text1_index-1][text2_index]:
        # if top is greater than left, go top
        lcs_set.update(self.backtrack_lcs_recursive_all(text1, text2, text1_index, text2_index-1, memo))
      elif memo[text1_index-1][text2_index] > memo[text1_index][text2_index-1]:
        # if left is greater than top, go left
        lcs_set.update(self.backtrack_lcs_recursive_all(text1, text2, text1_index-1, text2_index, memo))
      else:
        # both are equal, choose both
        lcs_set.update(self.backtrack_lcs_recursive_all(text1, text2, text1_index, text2_index-1, memo))
        lcs_set.update(self.backtrack_lcs_recursive_all(text1, text2, text1_index-1, text2_index, memo))
      return lcs_set

  def backtrack_all(self, text1, text2, i, j, memo, ans_set, ans):
    if i == 0 or j == 0:
      ans_set.add(ans)
      return
    elif text1[i - 1] == text2[j - 1]:
      ans = text1[i - 1] + ans
      self.backtrack_all(text1, text2, i - 1, j - 1, memo, ans_set, ans)
    else:
      if memo[i][j - 1] > memo[i - 1][j]:
        # if top is greater than left, go top
        self.backtrack_all(text1, text2, i, j - 1, memo, ans_set, ans)
      elif memo[i - 1][j] > memo[i][j - 1]:
        # if left is greater than top, go left
        self.backtrack_all(text1, text2, i - 1, j, memo, ans_set, ans)
      else:
        # both are equal, choose both
        self.backtrack_all(text1, text2, i, j - 1, memo, ans_set, ans)
        self.backtrack_all(text1, text2, i - 1, j, memo, ans_set, ans)

  def lcs(self, text1, text2):
    # bottom-up Dynamic Programming ??
    memo = self.generate_memo(text1, text2)
    for i in range(1, len(text1) + 1):
      for j in range(1, len(text2) + 1):
        if text1[i - 1] == text2[j - 1]:
          memo[i][j] = 1 + memo[i - 1][j - 1]
        else:
          memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    # return memo[-1][-1]
    # print(memo[-1][-1])
    # print self.backtrack_lcs(text1, text2, memo)
    # print self.backtrack_lcs_recursive_all(text1, text2, len(memo) - 1, len(memo[0]) - 1, memo)
    # print self.backtrack_lcs_recursive(text1, text2, len(memo)-1 , len(memo[0])-1, memo)
    ans = ''
    ans_set = set()
    self.backtrack_all(text1, text2, len(memo) - 1, len(memo[0]) - 1, memo, ans_set, ans)
    print ans_set

  def lcs1(self, text1, text2):
    # bottom-up Dynamic Programming ??
    if len(text1) < len(text2): text1, text2 = text2, text1
    curr = [0] * (len(text2) + 1)
    prev = [0] * (len(text2) + 1)
    for i in range(1, len(text1) + 1):
      for j in range(1, len(text2) + 1):
        if text1[i - 1] == text2[j - 1]:
          curr[j] = 1 + prev[j - 1]
        else:
          curr[j] = max(prev[j], curr[j - 1])
      prev, curr = curr, prev
    return prev[-1]

if __name__ == '__main__':
  sol = Solution()
  # text1 = 'abcde'
  # text2 = 'ace'
  text1 = 'AATCC'
  text2 = 'ACACG'
  # text1 = "ylqpejqbalahwr"
  # text2 = "yrkzavgdmdgtqpg"

  # print(sol.lcs_start(text1, text2))
  # print(sol.lcs_end(text1, text2))
  # print(sol.lcs(text1, text2))
  # text1 = 'intention'
  # text2 = 'execution'
  print(sol.lcs(text1, text2))
  # print(sol.lcs_recursive_start(text1, text2, 0, 0))
  # print(sol.lcs_recursive_end(text1, text2, len(text1) - 1, len(text2) - 1))
  pass