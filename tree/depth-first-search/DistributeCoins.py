'''
979. Distribute Coins in Binary
https://leetcode.com/problems/distribute-coins-in-binary-tree/

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4


Note:

1<= N <= 100
0 <= node.val <= N


'''
class SolutiondistributeCoins(object):
  def getpostorder(self, root):
    stack = []
    current = root
    rpo = []
    while current or stack:
      while current:
        rpo.append(current)
        stack.append(current)
        current = current.right
      current = stack.pop()
      current = current.left
    return list(reversed(rpo))

  def distribute_tree(self, subtree_root):
    moves = 0
    # Handle leaves having more
    if subtree_root.left and subtree_root.left.val > 1:
      subtree_root.val += subtree_root.left.val - 1
      moves = subtree_root.left.val - 1
      subtree_root.left.val = 1
    if subtree_root.right and subtree_root.right.val > 1:
      subtree_root.val += subtree_root.right.val - 1
      moves = subtree_root.right.val - 1
      subtree_root.right.val = 1
    # Handle leaves having less
    if subtree_root.left and subtree_root.val > 1 and subtree_root.left.val == 0:
      subtree_root.val -= 1
      subtree_root.left.val = 1
      moves += 1
    if subtree_root.right and subtree_root.val > 1 and subtree_root.right.val == 0:
      subtree_root.val -= 1
      subtree_root.right.val = 1
      moves += 1

    return moves

  def distributeCoins(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
      return None

    po = self.getpostorder(root)
    moves = 0
    while po:
      current = po.pop(0)
      moves += self.distribute_tree(current)
    return moves

if __name__ == '__main__':
  sol = SolutiondistributeCoins()
  root = NodeBinTree(4)
  root.left = NodeBinTree(0)
  root.left.right = NodeBinTree(0)
  root.left.right.right = NodeBinTree(0)

  print(sol.distributeCoins(root))