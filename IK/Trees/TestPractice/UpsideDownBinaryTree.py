"""
https://leetcode.com/problems/binary-tree-upside-down/

156. Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1
Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

"""


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Solution:
  def get_stacks(self, root, left, right):
    while root:
      left.append(root)
      right.append(root.right)
      root = root.left
    right.pop()

  def generate_tree(self, left, right):
    root, curr = None, None
    while left:
      curr = left.pop()
      if not root: root = curr
      curr.left = right.pop() if right else None
      curr.right = left[len(left)-1] if left else None
    return root

  def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
    if not root: return None
    left, right = [], []
    self.get_stacks(root, left, right)
    root = self.generate_tree(left, right)
    return root


if __name__ == '__main__':
  root = TreeNode(1)
  root.right = TreeNode(3)
  root.left = TreeNode(2)
  root.left.right = TreeNode(5)
  root.left.left = TreeNode(4)

  sol = Solution()
  newroot = sol.upsideDownBinaryTree(root)
