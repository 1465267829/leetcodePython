'''
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right and root.val == sum: return True
        sum  -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def hasPathSumReturnPath(self, root, sum):
      '''
      Return 1st path in the tree where the sum is found
      '''
      if not root: return []
      path = []

      def helper(root, sum, path):
        if not root: return None
        path.append(root.val)
        if not root.left and not root.right and root.val == sum: return path
        sum -= root.val
        return helper(root.left, sum, path) or helper(root.right, sum, path)

      return helper(root, sum, path)

    def hasPathSumReturnPaths(self, root, sum):
      '''
      Return all paths in the tree where the sum is found
      '''
      if not root: return []

      def helper(root, sum, path, paths):
        if not root: return None
        level_path = path[:]
        level_path.append(root.val)
        if not root.left and not root.right:
          if root.val == sum: paths.append(level_path)
          return None
        sum -= root.val
        return helper(root.left, sum, level_path, paths) or helper(root.right, sum, level_path, paths)

      path = []
      paths = []
      helper(root, sum, path, paths)
      return paths

    def printPaths(self, root):
      if not root: return 0

      def helper(root, path, paths):
        if not root: return
        level_path = path[:]
        level_path.append(root.val)
        if not root.left and not root.right:
          paths.append(level_path)
          return
        return helper(root.left, level_path, paths) or helper(root.right, level_path, paths)

      path = []
      paths = []
      helper(root, path, paths)
      return paths


'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/
129. Sum Root to Leaf Numbers
Medium

687

24

Favorite

Share
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

class SolutionSumNumbers(object):
  def sumNumbers(self, root):
    if not root: return 0

    def helper(root, path, paths):
      if not root: return
      level_path = path[:]
      level_path.append(root.val)
      if not root.left and not root.right:
        level_path = int(''.join(map(str, level_path)))
        paths.append(level_path)
        return
      return helper(root.left, level_path, paths) or helper(root.right, level_path, paths)

    path = []
    paths = []
    helper(root, path, paths)
    return sum(paths)

if __name__ == '__main__':
    # root = TreeNode(5)

    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    #
    # root.left.left = TreeNode(11)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    #
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.right.right = TreeNode(1)
    #
    # sol = Solution()
    # print(sol.hasPathSum(root, 22))
    # print(sol.hasPathSumReturnPath(root, 22))

    # root = TreeNode(5)
    #
    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    #
    # root.left.left = TreeNode(11)
    # root.right.left = TreeNode(9)
    # root.right.right = TreeNode(4)
    #
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.right.right = TreeNode(15)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    sol = Solution()
    # print(sol.hasPathSumReturnPaths(root, 22))
    print(sol.printPaths(root))
    # print(sol.printPathsIterativeUsingMap(root))

    # sol = SolutionSumNumbers()
    # print(sol.sumNumbers(root))
