'''
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num
    
class SolutionIncreasingBST(object):
  def increasingBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root: return None

    current = root
    stack = []
    previous_inorder = None
    ret = None
    while current or stack:
      while current:
        stack.append(current)
        current = current.left
      current = stack.pop()
      # visit
      if not ret: ret = current
      if previous_inorder:
        previous_inorder.right = current
        previous_inorder.left = None
      previous_inorder = current
      current = current.right
    return ret

if __name__ == '__main__':
  root = TreeNode(5)
  root.left = TreeNode(3)
  root.right = TreeNode(6)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(4)
  root.right.right = TreeNode(8)
  root.left.left.left = TreeNode(1)
  root.right.right.left = TreeNode(7)
  root.right.right.right = TreeNode(9)

  sol = SolutionIncreasingBST()
  root = sol.increasingBST(root)
  pass
