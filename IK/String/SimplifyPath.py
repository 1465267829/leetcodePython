'''
https://leetcode.com/problems/simplify-path/

71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
'''


class Solution:
  def simplifyPath(self, path: str) -> str:
    if not str: return ''
    final_stack = []
    init_stack = path.split('/')
    for item in init_stack:
      if item == '..':
        if final_stack: final_stack.pop()
      elif item == '.' or item == '':
        pass
      else:
        final_stack.append(item)
    ans = '/' + '/'.join(final_stack)
    return ans


if __name__ == '__main__':
    sol = Solution()
    # path = '/home/'
    # path = '/../'
    # path = '//'
    path = '/home//foo/'
    print(sol.simplifyPath(path))
