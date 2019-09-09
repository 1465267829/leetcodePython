'''
https://leetcode.com/problems/binary-tree-upside-down/
156. Binary Tree Upside Down
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def weirdOrder(self, root):
    queue = []
    queue.append(root)
    result = []
    weird_order_list = []
    while queue:
      current_level = []
      for _ in range(len(queue)):
        current = queue.pop(0)
        current_level.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
      for current_element in reversed(current_level):
        result.append(current_element)

    for element in reversed(result):
      weird_order_list.append(element)
    return weird_order_list

  def swapleftright(self, root):
    if not root: return None
    if not root.left or not root.right: return root
    root.left = self.swapleftright(root.left)
    root.right = self.swapleftright(root.right)
    if root.left and root.right:
      root.left.val, root.right.val = root.right.val, root.left.val
    elif not root.left and root.right:
      root.left.val, root.right = root.right.val, None
    elif not root.right and root.left:
      root.left.val, root.right.val = None, root.left.val
    return root

  def upsideDownBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root: return None
    weird_order_list = self.weirdOrder(root)
    new_root_value = weird_order_list.pop(0)
    new_root = TreeNode(new_root_value)
    current_root = new_root
    for element in weird_order_list:
      if not current_root.right:
        current_root.right = TreeNode(element)
        continue
      if not current_root.left:
        current_root.left = TreeNode(element)
        current_root = current_root.left
        continue
    new_root_foo = self.swapleftright(new_root)
    return new_root_foo

if __name__ == '__main__':
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  # root.right = TreeNode(3)
  # root.right.left = TreeNode(6)
  # root.right.right = TreeNode(7)
  sol = Solution()
  sol.upsideDownBinaryTree(root)