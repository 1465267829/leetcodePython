'''
1110. Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionOld(object):
    # def getParentMap(self, root):
    #   parentMap = {}
    #   parentMap[root.val] = None
    #   queue = []
    #   queue.append(root)
    #   while queue:
    #     current = queue.pop(0)
    #     if current.left:
    #       queue.append(current.left)
    #       parentMap[current.left.val] = current
    #     if current.right:
    #       queue.append(current.right)
    #       parentMap[current.right.val] = current
    #   return parentMap

    # def dfs(self, root, to_delete_set, parentMap, result):
    #   if not root: return
    #   self.dfs(root.left, to_delete_set, parentMap, result)
    #   self.dfs(root.right, to_delete_set, parentMap, result)
    #   root_parent = parentMap[root.val]
    #
    #   if root.val in to_delete_set:
    #     # update parent, one of the child node is deleted
    #     if root_parent and root_parent.left.val == root.val: root_parent.left = None
    #     if root_parent and root_parent.right.val == root.val: root_parent.right = None
    #
    #     # if any child(ren) exist then add then to forest
    #     if root.left: result.append(root.left)
    #     if root.right: result.append(root.right)
    #   pass

    # def dfs(self, root, to_delete_set, parentMap, result, parent):
    def dfs(self, root, to_delete_set, result, parent):
      if not root: return
      # self.dfs(root.left, to_delete_set, parentMap, result, root)
      # self.dfs(root.right, to_delete_set, parentMap, result, root)
      self.dfs(root.left, to_delete_set, result, root)
      self.dfs(root.right, to_delete_set, result, root)
      # root_parent = parentMap[root.val]

      if root.val in to_delete_set:
        # update parent, one of the child node is deleted
        if parent and parent.left and parent.left.val == root.val: parent.left = None
        if parent and parent.right and parent.right.val == root.val: parent.right = None

        # if any child(ren) exist then add then to forest
        if root.left: result.append(root.left)
        if root.right: result.append(root.right)
      pass

    def addRootIfNeeded(self, root, result, to_delete_set):
      if root.val not in to_delete_set:
        result.append(root)

    def delNodes(self, root, to_delete):
      """
      :type root: TreeNode
      :type to_delete: List[int]
      :rtype: List[TreeNode]
      """
      to_delete_set = set(to_delete)
      # parentMap = self.getParentMap(root)
      result = []
      self.addRootIfNeeded(root, result, to_delete_set)
      # self.dfs(root, to_delete_set, parentMap, result, None)
      self.dfs(root, to_delete_set, result, None)
      return result

class Solution(object):
  def dfs(self, root, to_delete_set, result, parent):
    if not root: return
    self.dfs(root.left, to_delete_set, result, root)
    self.dfs(root.right, to_delete_set, result, root)

    if root.val in to_delete_set:
      # update parent, one of the child node is deleted
      if parent and parent.left and parent.left.val == root.val: parent.left = None
      if parent and parent.right and parent.right.val == root.val: parent.right = None

      # if any child(ren) exist then add then to forest
      if root.left: result.append(root.left)
      if root.right: result.append(root.right)
    pass

  def addRootIfNeeded(self, root, result, to_delete_set):
    if root.val not in to_delete_set:
      result.append(root)

  def delNodes(self, root, to_delete):
    """
    :type root: TreeNode
    :type to_delete: List[int]
    :rtype: List[TreeNode]
    """
    to_delete_set = set(to_delete)
    result = []
    self.addRootIfNeeded(root, result, to_delete_set)
    self.dfs(root, to_delete_set, result, None)
    return result

if __name__ == '__main__':

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right = TreeNode(3)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  sol = Solution()
  sol.delNodes(root, [7, 1, 2])