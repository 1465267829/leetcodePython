'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def levelorderTraversal(self, root):
      if not root:
        return []
      curr = root
      queue = [curr]
      ret = []
      while queue:
        level = []
        for _ in range(len(queue)):
          curr = queue.pop(0)
          level.append(curr.val)
          if curr.left:
            queue.append(curr.left)
          if curr.right:
            queue.append(curr.right)
        ret.append(level)
      return ret

  def buildTreePreorderInorder(self, preorder, inorder):
    inorder_dict = { value : index for index, value in enumerate(inorder)}
    preorder_iter = iter(preorder)

    def helper(start, end):
      if start > end: return None
      root_val = next(preorder_iter)
      root = TreeNode(root_val)
      inorder_index = inorder_dict[root_val]
      root.left =  helper(start, inorder_index - 1)
      root.right = helper(inorder_index + 1, end)
      return root

    return helper(0, len(inorder) - 1)

  def buildTreePostorderInorder(self, postorder, inorder):
    inorder_dict = { value : index for index, value in enumerate(inorder)}
    postorder_iter = iter(reversed(postorder))

    def helper(start, end):
      if start > end: return None
      root_val = next(postorder_iter)
      root = TreeNode(root_val)
      inorder_index = inorder_dict[root_val]
      root.right = helper(inorder_index + 1, end)
      root.left =  helper(start, inorder_index - 1)
      return root

    return helper(0, len(inorder) - 1)

if __name__ == "__main__":
  sol = Solution()
  preorder = [3, 9, 20, 15, 7]
  inorder = [9, 3, 15, 20, 7]
  root =  sol.buildTreePreorderInorder(preorder, inorder)
  print(sol.levelorderTraversal(root))
