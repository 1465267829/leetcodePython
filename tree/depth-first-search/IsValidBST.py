class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num
'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
'''
class SolutionisValidBST(object):
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
      return True
    stack = []
    previous = None
    current = root
    while current or stack:
      while current:
        stack.append(current)
        current = current.left
      current = stack.pop()
      if previous and (previous.val >= current.val):
        return False
      previous = current
      current = current.right
    return True

if __name__ == '__main__':

  root = TreeNode(5)
  root.left = TreeNode(1)
  root.right = TreeNode(6)
  root.right.left = TreeNode(4)
  root.right.right = TreeNode(7)

  root = TreeNode(2)
  root.left = TreeNode(1)
  root.right = TreeNode(3)

  s = SolutionisValidBST()
  print(s.isValidBST(root))