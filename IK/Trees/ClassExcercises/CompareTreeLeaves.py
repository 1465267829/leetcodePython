"""
https://leetcode.com/problems/leaf-similar-trees/
https://www.geeksforgeeks.org/check-if-leaf-traversal-of-two-binary-trees-is-same/

Use iterators, both recursive and iterative
"""

from IK.Trees.ClassExcercises.Tree import TreeNode


class Solution:
  @classmethod
  def leaf_iterator(cls, root):
    if root.left is None and root.right is None:
      yield root.val
    if root.left:
      yield from cls.leaf_iterator(root.left)
    if root.right:
      yield from cls.leaf_iterator(root.right)

  def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    root1_iter = Solution.leaf_iterator(root1)
    root2_iter = Solution.leaf_iterator(root2)

    while True:
      current_root1_leaf = next(root1_iter, None)
      current_root2_leaf = next(root2_iter, None)
      if current_root1_leaf is None and current_root2_leaf is None:
        break
      if current_root1_leaf and current_root2_leaf and current_root1_leaf != current_root2_leaf:
        return False
      if current_root1_leaf is None or current_root2_leaf is None:
        return False
    return True


if __name__ == '__main__':
  root1 = TreeNode(1)
  root1.left = TreeNode(2)
  root1.right = TreeNode(3)
  root1.left.left = TreeNode(4)
  root1.right.left = TreeNode(6)
  root1.right.right = TreeNode(7)

  root2 = TreeNode(0)
  root2.left = TreeNode(5)
  root2.right = TreeNode(8)
  root2.left.right = TreeNode(4)
  root2.right.left = TreeNode(6)
  root2.right.right = TreeNode(7)

  # root1 = TreeNode(0)
  # root1.left = TreeNode(1)
  # root1.right = TreeNode(2)
  # root1.left.left = TreeNode(8)
  # root1.left.right = TreeNode(9)
  #
  # root2 = TreeNode(1)
  # root2.left = TreeNode(4)
  # root2.right = TreeNode(3)
  # root2.left.right = TreeNode(8)
  # root2.right.left = TreeNode(2)
  # root2.right.right = TreeNode(9)

  sol = Solution()
  print(sol.leafSimilar(root1, root2))





