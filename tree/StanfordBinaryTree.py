'''
http://cslibrary.stanford.edu/110/BinaryTrees.html
'''
class TreeNode:
  def __init__(self, num):
    self.left = None
    self.right = None
    self.val = num

def lookup(root, target):
  if not root: return False
  if root.val == target: return True
  return lookup(root.left, target) or lookup(root.right, target)

def insert(root, data):
  if not root: return TreeNode(data)
  if data <= root.val:
    root.left = insert(root.left, data)
  else:
    root.right = insert(root.right, data)
  return root

def build123(root):
  data = [2, 1, 3]
  root = None
  for elem in data:
    root = insert(root, elem)
  return root

def size(root):
  if not root: return 0
  return 1 + size(root.left) + size(root.right)

def maxdepth(root):
  if not root: return 0
  return 1 + max(maxdepth(root.left), maxdepth(root.right))

def minvalue(root):
  if not root: return -1
  current = root
  while current.left:
    current = current.left
  return current.val

def hasPathSum(root, sum):
  if not root: return sum == 0
  curr_sum = sum - root.val
  return hasPathSum(root.left, curr_sum) or hasPathSum(root.right, curr_sum)

def printPaths(root):
  def helper(r, cp, ps):
    if not r: return
    cp = cp[:]
    cp.append(r.val)
    if not r.left and not r.right:
        ps.append(cp)
        return
    helper(r.left, cp, ps)
    helper(r.right, cp, ps)
    return
  if not root: return
  paths = []
  current_path = []
  helper(root, current_path, paths)
  return paths

def mirror(root):
  if not root: return
  mirror(root.left)
  mirror(root.right)
  root.left, root.right = root.right, root.left
  return root

def doubleTree(root):
  if not root: return
  doubleTree(root.left)
  doubleTree(root.right)
  oldleft = root.left
  root.left = TreeNode(root.val)
  root.left.left = oldleft
  return root6

def sameTree(a, b):
  if not a and not b: return True
  if not a or not b: return False
  return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right)

def isBST(root):
  def helper(root, current_range):
    if not root: return True
    if not (minint <= root.val < maxint): return False
    return helper(root.left, [current_range[0], root.val]) or helper(root.right, [root.val + 1, current_range[1]])
  import sys
  maxint = sys.maxsize
  minint = -maxint - 1
  current_range = [minint, maxint]
  return helper(root, current_range)

def treeToList(root):
  '''
  http://cslibrary.stanford.edu/109/TreeListRecursion.html
  '''
  def join(a, b):
    a.right = b
    b.left = a
  def append(a, b):
    if not a: return b
    if not b: return a
    alast = a.left
    blast = b.left
    join(alast, b)
    join(blast, a)
    return a
  if not root: return None
  leftlist = treeToList(root.left)
  rightlist = treeToList(root.right)
  root.left = root.right = root
  root = append(leftlist, root)
  root = append(root, rightlist)
  return root
# def treeToListIter(root):
#   if not root: return None
#   stack = []
#   current = root
#   head = None
#   previous_inorder = None
#   while current or stack:
#     while current:
#       stack.append(current)
#       current = current.left
#     current = stack.pop()
#     # visit
#     if not head: head = current
#     if previous_inorder:
#       previous_inorder.right = current
#       current.left = previous_inorder
#     previous_inorder = current
#     current = current.right
#   previous_inorder.right = head
#   head.left = previous_inorder
#   return head

def treeToListIter(root):
  def inorder(root):
    stack = []
    current = root
    while current or stack:
      while current:
        stack.append(current)
        current = current.left
      current = stack.pop()
      yield current
      current = current.right

  previous_inorder, head = None, None

  for current in inorder(root):
    if not head: head = current
    if previous_inorder:
      previous_inorder.right = current
      current.left = previous_inorder
    previous_inorder = current

  head.left = previous_inorder
  previous_inorder.right = head
  return head

if __name__ == '__main__':
  root = TreeNode(5)
  root.left = TreeNode(3)
  root.right = TreeNode(8)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(4)
  root.left.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(10)
  root.right.left.right = TreeNode(7)
  root.right.right.left = TreeNode(9)

  # print(lookup(root, 10))
  # print(size(root))
  # print(minvalue(root))
  # print(printPaths(root))
  # print(mirror(root))
  # print(mirror(root))

  # a = TreeNode(5)
  # a.left = TreeNode(3)
  # a.right = TreeNode(8)
  # a.left.left = TreeNode(2)
  # a.left.right = TreeNode(4)
  # a.left.left.left = TreeNode(1)
  # a.right.left = TreeNode(6)
  # a.right.right = TreeNode(10)
  # a.right.left.right = TreeNode(7)
  # a.right.right.left = TreeNode(9)

  # b = TreeNode(5)
  # b.left = TreeNode(3)
  # b.right = TreeNode(8)
  # b.left.left = TreeNode(2)
  # b.left.right = TreeNode(4)
  # b.left.left.left = TreeNode(1)
  # b.right.left = TreeNode(6)
  # b.right.right = TreeNode(10)
  # b.right.left.right = TreeNode(7)
  # b.right.right.left = TreeNode(9)
  #
  # print(sameTree(a, b))
  # print(isBST(root))
  # l = treeToList(root)
  l = treeToListIter(root)
  pass