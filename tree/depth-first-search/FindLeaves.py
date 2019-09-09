'''
https://leetcode.com/problems/find-leaves-of-binary-tree/
366. Find Leaves of Binary Tree
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num

class SolutionFindLeaves(object):
  def findLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return

    def generate_parent_map(root):
      parent_map = {}
      parent_map[root.val] = None
      queue = []
      current = root
      queue.append(current)
      parent = None
      while queue:
        print('   ')
        for _ in range(len(queue)):
          current = queue.pop(0)
          parent = current
          if current.left:
            parent_map[current.left.val] = parent
            queue.append(current.left)
          if current.right:
            parent_map[current.right.val] = parent
            queue.append(current.right)
      return parent_map

    def generate_height_list(root):
      res = []
      def dfs(root):
        if not root: return -1
        height = 1 + max(dfs(root.left), dfs(root.right))
        if height >= len(res): res.append([])
        res[height].append(root.val)
        return height
      dfs(root)
      return res

    parent_map = generate_parent_map(root)
    height_list = generate_height_list(root)
    for current_height in height_list:
      # print('Current height [{}]'.format(current_height))
      for element in current_height:
        parent = parent_map[element]
        if parent and parent.left and parent.left.val == element:
            parent.left = None
        if parent and parent.right and parent.right.val == element:
            parent.right = None

if __name__ == '__main__':
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  sol = SolutionFindLeaves()
  sol.findLeaves(root)