# def palindrom(s, start, end):
#   # Base
#   if start > end:
#     return True
#   # Recurse
#   if s[start] != s[end]:
#     return False
#   else:
#     return palindrom(s, start+1, end-1)
#
#
# def generate_palindromic_decompositions(s):
#   # result = set()
#   result = []
#   for i in range(len(s)):
#     for j in range(i, len(s)):
#       if palindrom(s, i, j):
#         # result.add(s[i:j+1])
#         result.append(s[i:j+1])
#     print(result)
#   return list(result)


# def generate_palindromic_decompositions(string):
#   if not string or len(string) == 1:
#     return [string]
#
#   output = []
#   n = len(string)
#
#   def _palindromic_decomposition(so_far, start):
#     # base case
#     if start == n:
#       output.append('|'.join(so_far))
#       return
#
#     # take every possible string from the current position and if it's palndromic go forward, and if it's not prune
#     for i in range(start + 1, n + 1):
#       curr = string[start:i]
#       if is_palindrome(curr):
#         so_far.append(curr)
#         _palindromic_decomposition(so_far, i)
#         # at the end of dfs remove what was appended to
#         so_far.pop()
#
#   so_far, start = [], 0
#   _palindromic_decomposition(so_far, start)
#   return output
#
#
# def is_palindrome(string):
#   if not string or len(string) == 1:
#     return True
#
#   low, high = 0, len(string) - 1
#   while low < high:
#     if string[low] != string[high]:
#       return False
#     low += 1
#     high -= 1
#
#   return True
#
#
# def is_palindrome_rec(string):
#   if len(string) == 0:
#     return True
#   return _is_palindrome(string, 0, len(string) - 1)
#
#
# def _is_palindrome(string, start, end):
#   # empty string or string of 1 character
#   if start == end or start > end:
#     return True
#
#   return string[start] == string[end] and _is_palindrome(string, start + 1, end - 1)

# class Solution(object):
#   def partition(self, s):
#     """
#     :type s: str
#     :rtype: List[List[str]]
#     """
#     if not s:
#       return []
#     ans = []
#     self.helper(s, [], ans)
#     return ans
#
#   def helper(self, s, curr, res):
#     if not s:
#       # res.append(curr)
#       res.append('|'.join(curr))
#       return
#     for i in range(len(s)):
#       current = s[:i + 1]
#       if self.isPali(current):
#         temp_0 = s[i + 1:]
#         temp_1 = curr + [current]
#         self.helper(temp_0, temp_1, res)
#
#   def isPali(self, string):
#     left, right = 0, len(string) - 1
#     while left < right:
#       if string[left] != string[right]:
#         return False
#       left += 1
#       right -= 1
#     return True

def isPali(string):
  left, right = 0, len(string) - 1
  while left < right:
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1
  return True


def helper(s, curr, res):
  if not s:
    res.append('|'.join(curr))
    return
  for i in range(len(s)):
    current = s[:i + 1]
    if isPali(current):
      temp_0 = s[i + 1:]
      temp_1 = curr + [current]
      helper(temp_0, temp_1, res)


def generate_palindromic_decompositions(s):
  if not s:
    return []
  ans = []
  helper(s, [], ans)
  return ans

if __name__ == '__main__':
  # print(generate_palindromic_decompositions('abracadabra'))
  # print(generate_palindromic_decompositions('abcba'))
  # print generate_palindromic_decompositions('abaccdaba')
  # print generate_palindromic_decompositions('abracadabra')
  # print(generate_palindromic_decompositions('abba'))
  generate_palindromic_decompositions('abba')
  # sol = Solution()
  # print(sol.partition('aba'))