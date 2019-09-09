
'''
1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num

class SolutionMaxAncestorDiff(object):
  def maxAncestorDiff(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0
    self.maxdiff = 0

    def helper(root, maxleft, maxright):
      if not root: return
      if root.val < maxleft:
        maxleft = root.val
      if root.val > maxright:
        maxright = root.val
      self.maxdiff = max(self.maxdiff, abs(maxleft - maxright))
      return helper(root.left, maxleft, maxright) or helper(root.right, maxleft,
                                                            maxright)

    helper(root, root.val, root.val)
    return self.maxdiff

if __name__ == '__main__':
  root = TreeNode(8)
  root.left = TreeNode(3)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(6)
  root.left.right.left = TreeNode(4)
  root.left.right.right = TreeNode(7)
  root.right = TreeNode(10)
  root.right.right = TreeNode(14)
  root.right.right.left = TreeNode(13)

  sol = SolutionMaxAncestorDiff()
  print(sol.maxAncestorDiff(root))