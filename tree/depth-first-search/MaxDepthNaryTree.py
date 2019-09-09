'''
559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
  def __init__(self, val, children):
    self.val = val
    self.children = children

class SolutionmaxDepth(object):
  def maxDepth(self, root):
    """
    :type root: Node
    :rtype: int
    """
    if not root:
      return 0

    max_depth = 0
    queue = [root, None]
    while queue:
      current = queue.pop(0)
      if not current:
        max_depth += 1
        if not queue:
          break
        queue.append(None)
        continue
      if current.children:
        for c in current.children:
          queue.append(c)
    return max_depth

if __name__ == '__main__':
  five = Node(5, [])
  six = Node(6, [])
  two = Node(2, [])
  four = Node(4, [])
  three = Node(3, [five, six])
  one = Node(1, [three, two, four])
  root = one

  s = SolutionmaxDepth()
  print(s.maxDepth(root))