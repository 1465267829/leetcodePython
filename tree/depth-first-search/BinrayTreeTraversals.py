
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# A utility function to insert a new node with the given key
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def createBinaryTree(elements_list):
  root = TreeNode(elements_list[0])
  for i in range(1, len(elements_list)):
    insert(root, TreeNode(elements_list[i]))
  return root

class Solution(object):
  def preorderRecusive(self, root):
    def helper(root, returnList):
      if root:
        returnList.append(root.val)
        helper(root.left, returnList)
        helper(root.right, returnList)

    preorderList = []
    helper(root, preorderList)
    return preorderList

  def preorderIterative(self, root):
    if not root:
      return []
    stack = []
    ret = []
    curr = root
    while stack or curr:
      while curr:
        ret.append(curr.val)
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      curr = curr.right
    return ret

  def inorderRecursive(self, root):
    def helper(root, returnList):
      if root:
        helper(root.left, returnList)
        returnList.append(root.val)
        helper(root.right, returnList)
    preorderList = []
    helper(root, preorderList)
    return preorderList

  def inorderIterative(self, root):
    if not root:
      return []
    stack = []
    ret = []
    curr = root
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      ret.append(curr.val)
      curr = curr.right
    return ret

  def postorderRecursive(self, root):
    def helper(root, returnList):
      if root:
        helper(root.left, returnList)
        helper(root.right, returnList)
        returnList.append(root.val)
    postorderList = []
    helper(root, postorderList)
    return postorderList

  def postorderIterative(self, root):
    if not root:
      return []
    stack = []
    ret = []
    curr = root
    while curr or stack:
      while curr:
        ret.append(curr.val)
        stack.append(curr)
        curr = curr.right
      curr = stack.pop()
      curr = curr.left
    return list(reversed(ret))

  def levelorder(self, root):
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

def preorderGenerator(root):
  if not root: yield
  stack = []
  current = root
  while current or stack:
    while current:
      yield current.val
      stack.append(current)
      current = current.left
    current = stack.pop()
    current = current.right

def inorderGenerator(root):
  if not root: yield
  stack = []
  current = root
  while current or stack:
    while current:
      stack.append(current)
      current = current.left
    current = stack.pop()
    yield current.val
    current = current.right

def postorderGenerator(root):
  '''Don't know how. postOrderIterative needs to see the entire list'''
  pass

def levelorderGenerator(root):
  if not root: yield
  queue = []
  current = root
  queue.append(current)
  while queue:
    level = []
    for _ in range(len(queue)):
      current = queue.pop(0)
      # yield current.val # Flat list
      level.append(current.val)
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
    yield level

class BinaryTreeMultipleIterator:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

  def breadth_first_inorder(self):
    stack = []
    current = self
    while current or stack:
      while current:
        stack.append(current)
        current = current.left
      current = stack.pop()
      yield current.value
      current = current.right


  def depth_first(self):
    pass

class SolutionDepthFirstBinaryTreeNonMarker(object):
  def dfs(self, root):
    if not root: return []

    queue = [root]
    level = 1
    bfs = {}
    while queue:
      current_level = []
      for _ in range(len(queue)):
        current = queue.pop(0)
        current_level.append(current.val)
        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)
      bfs[level] = current_level
      level += 1
    return bfs

# if __name__ == '__main__':
#   # root = Node(5)
#   #
#   # root.left = Node(2)
#   # root.right = Node(8)
#   #
#   # root.left.left = Node(1)
#   # root.left.right = Node(4)
#   # root.right.left = Node(7)
#   # root.right.right = Node(9)
#   #
#   # root.left.right.left = Node(3)
#   # root.right.left.left = Node(6)
#
#   root = NodeBinTree(5)
#   root.left = NodeBinTree(2)
#   root.left.right = NodeBinTree(4)
#   root.right = NodeBinTree(7)
#   root.right.right = NodeBinTree(8)
#
#   s = SolutionDepthFirstBinaryTreeNonMarker()
#   print(s.dfs(root))

if __name__ == "__main__":
  sol = Solution()
  root = createBinaryTree([50, 30, 20, 40, 70, 60, 80])
  # print(sol.preorderRecusive(root))
  # print(sol.preorderIterative(root))
  # print(sol.inorderRecursive(root))
  print(sol.inorderIterative(root))
  # print(sol.postorderRecursive(root))
  # print(sol.postorderIterative(root))
  # print(sol.levelorder(root))

  # print(list(preorderGenerator(root)))
  # print(list(preorderGenerator(root)))
  # print(list(levelorderGenerator(root)))

  sol_multiple_iter = BinaryTreeMultipleIterator(root)
  print(sol_multiple_iter.breadth_first_inorder())