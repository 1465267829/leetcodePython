from IK.Trees.ClassExcercises import Tree


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def generate_from_inorder_preorder(self, inorder, preorder):
    def helper(inorder, preorder):
      if len(preorder) == 0: return None
      root = Tree.TreeNode(preorder[0])
      root_index = inorder.index(root.val)
      root.left = helper(inorder[:root_index], preorder[1: 1+root_index])
      root.right = helper(inorder[root_index+1:], preorder[root_index+1:])
      return root
    self.root = helper(inorder, preorder)

  def generate_from_inorder_postorder(self, inorder, postorder):
    def helper(inorder, postorder):
      if len(postorder) == 0: return None
      root = Tree.TreeNode(postorder[-1])
      root_index = inorder.index(root.val)
      root.left = helper(inorder[:root_index], postorder[:root_index])
      root.right = helper(inorder[root_index+1:], postorder[root_index:len(postorder)-1])
      return root
    self.root = helper(inorder, postorder)

  def insert(self, key):
    if not self.root:
      self.root = Tree.TreeNode(key)
      return

    prev, curr = None, self.root

    while curr:
      if key < curr.val:
        prev = curr
        curr = curr.left
      else:
        prev = curr
        curr = curr.right

    if key < prev.val:
      prev.left = Tree.TreeNode(key)
    else:
      prev.right = Tree.TreeNode(key)

  def search(self, key):
    curr = self.root
    while curr:
      if key == curr.val:
        return curr
      elif key < curr.val:
        curr = curr.left
      else:
        curr = curr.right
    return None

  def find_successor(self, key):
    # key is assured to be present and no duplicates
    # search for the key and note the prev
    # foo points to parent of the node where,
    # the current path in the tree took last left turn
    prev, foo, curr = None, None, self.root
    while curr:
      if key == curr.val:
        # found the key: break
        break
      elif key < curr.val:
        # go left
        foo = curr
        prev = curr
        curr = curr.left
      else:
        # go right
        prev = curr
        curr = curr.right

    # here prev is None if the found node has no parent
    # i.e found node is root

    if curr.right:
      # case 0:
      # found node (curr) which has right child/subtree
      # find the minimum of right subtree and that the ans
      curr = curr.right
      while curr.left:
        curr = curr.left
      return curr
    else:
      # case 1, 2, 3
      # found node (curr) which has no right node/subtree
      if not prev:
        # case 1:
        # found node (curr) which has no right node/subtree
        # found node has no parent
        # found node has no successor
        return None
      else:
        # case 2 and 3
        # found node (curr) which has no right node/subtree
        # found node has parent
        if prev.left == curr:
          # case 2:
          # found node (curr) which has no right node/subtree
          # found node has parent
          # found node is left child of it's parent
          # found node's parent is the successor
          return prev
        elif prev.right == curr:
          # case 3:
          # found node (curr) which has no right node/subtree
          # found node has parent
          # found node is right child of it's parent
          # walk up the ancestors and note the right turn
          return foo

  def find_predecessor(self, key):
    # key is assured to be found, no dups
    # search for the key
    # foo points to parent of the node where,
    # the current path in the tree took last left right
    prev, foo, curr = None, None, self.root
    while curr:
      if key == curr.val:
        # found the key: break
        break
      elif key < curr.val:
        # go left
        prev = curr
        curr = curr.left
      else:
        # go right
        foo = curr
        prev = curr
        curr = curr.right

    # here prev is None is found node has no parent
    # i.e found node is root
    if curr.left:
      # case 0:
      # found node (curr) which has left child/subtree
      # find the maximum of left subtree and that the ans
      curr = curr.left
      while curr.right:
        curr = curr.right
      return curr
    else:
      # case 2 and 3
      # found node (curr) which has no left node/subtree
      # found node has parent
      if prev.right == curr:
        # case 2:
        # found node (curr) which has no left node/subtree
        # found node has parent
        # found node is right child of it's parent
        # found node's parent is the successor
        return prev
      elif prev.left == curr:
        # case 3:
        # found node (curr) which has no left node/subtree
        # found node has parent
        # found node is left child of it's parent
        # walk up the ancestors and note the left turn
        return foo

  def delete(self, key):
    # key is assured to be present and no duplicates
    # search for the key and note the prev
    prev, curr = None, self.root
    while curr:
      if key == curr.val:
        # found the key: break
        break
      elif key < curr.val:
        # go left
        prev = curr
        curr = curr.left
      else:
        # go right
        prev = curr
        curr = curr.right

    # here prev is None if the found node has no parent
    # i.e found node is root
    if not curr.left and not curr.right:
      # order of placing these cases is important
      # case 0:
      # to be deleted node doesn't have any children
      if prev:
        if curr == prev.left:
          # case 0.1 :
          # if current node is left child of it's parent
          # set parent's left child as None
          prev.left = None
        else:
          # case 0.2 :
          # if current node is right child of it's parent
          # set parent's right child as None
          prev.right = None
      else:
        # prev node doesn't exist, curr node is root
        # and root has no children
        self.root = None
    elif curr.left and curr.right:
      # case 1:
      # to be deleted node has both left and right tree
      # find if curr has a predecessor
      predecessor = self.find_predecessor(key)
      predecessor.val, curr.val = curr.val, predecessor.val

      # predecessor can have no child or only left child
      # predecessor can only be in left
      curr.left = predecessor.left
    else:
      # case 2:
      # to be deleted node has either left or right tree
      # determine which child exists
      child = curr.left if curr.left else curr.right
      if prev:
        # determine if the current element is left or right child
        # of it's parents
        if prev.left == curr:
          prev.left = child
        else:
          prev.right = child
      else:
        # to be deleted node is one child
        # to be deleted node has no parent
        # promote the child to root
        self.root = child
        curr.left, curr.right = None, None

  def preorder_recursive(self):
    def helper(root, result):
      if root:
        result.append(root.val)
        helper(root.left, result)
        helper(root.right, result)
    result = []
    helper(self.root, result)
    return result

  def inorder_recursive(self):
    def helper(root, result):
      if root:
        helper(root.left, result)
        result.append(root.val)
        helper(root.right, result)
    result = []
    helper(self.root, result)
    return result

  def postorder_recursive(self):
    def helper(root, result):
      if root:
        helper(root.left, result)
        helper(root.right, result)
        result.append(root.val)
    result = []
    helper(self.root, result)
    return result

  # depth first searches
  def preorder_iterative(self):
    curr = self.root
    stack = []
    result = []
    while stack or curr:
      while curr:
        result.append(curr.val)
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      curr = curr.right
    return result

  # depth first searches
  def preorder_iterative_generator(self):
    curr = self.root
    stack = []
    while stack or curr:
      while curr:
        yield curr.val
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      curr = curr.right

  # depth first searches
  def inorder_iterative(self):
    curr = self.root
    stack = []
    result = []
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      result.append(curr.val)
      curr = curr.right
    return result

  def inorder_iterative_generator(self):
    curr = self.root
    stack = []
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      yield curr.val
      curr = curr.right

  # depth first searches
  def postorder_iterative(self):
    curr = self.root
    stack = []
    result = []
    while stack or curr:
      while curr:
        result.append(curr.val)
        stack.append(curr)
        curr = curr.right
      curr = stack.pop()
      curr = curr.left
    return list(reversed(result))

  # breadth first searches
  def level_order(self):
    queue = []
    result = []
    queue.append(self.root)
    level = 0
    while queue:
      level_elements = []
      for _ in range(len(queue)):
        current = queue.pop(0)
        level_elements.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
      result.append(level_elements)
      level += 1
    return result

  @classmethod
  def leaf_node_generator_yield(cls, root):
    # learning:
    # https://stackoverflow.com/questions/38254304/can-generators-be-recursive
    # i am not sure how to avoid passing root
    # making it a classmethod, i.e ~static method
    if root.left is None and root.right is None:
      yield root.val
    if root.left:
      yield from cls.leaf_node_generator_yield(root.left)
    if root.right:
      yield from cls.leaf_node_generator_yield(root.right)

  @classmethod
  def tree_branches_generator_yield(cls, root, stack):
    if root.left is None and root.right is None:
      yield stack[:] + [root.val]

    stack.append(root.val)
    if root.left:
      yield from cls.tree_branches_generator_yield(root.left, stack)
    if root.right:
      yield from cls.tree_branches_generator_yield(root.right, stack)
    stack.pop()


if __name__ == '__main__':
  bst = BinarySearchTree()
  # nums = [4, 2, 3, 1, 5, 8, 7, 6]
  nums = [170, 150, 75, 87, 85, 80, 90, 110, 100]

  # insert
  for num in nums: bst.insert(num)

  # search test
  # for test in nums:
  #   print(bst.search(test).val)

  # find_successor test
  # sorted_nums = sorted(nums)
  # for test in sorted_nums:
  #   successor = bst.find_successor(test)
  #   successor = successor.val if successor else None
  #   print('Successor of {} is {}'.format(test, successor))

  # find_predecessor test
  # sorted_nums = sorted(nums)
  # for test in sorted_nums:
  #   predecessor = bst.find_predecessor(test)
  #   predecessor = predecessor.val if predecessor else None
  #   print('Predecessor of {} is {}'.format(test, predecessor))

  # delete test
  # reversed_sorted_nums = sorted(nums, reverse=True)
  # print(reversed_sorted_nums)
  # for test in reversed_sorted_nums:
  #   print('Deleting {}...'.format(test))
  #   bst.delete(test)
  #   print('Deleted {}...'.format(test))
  # print(bst.root)

  # preorder_recursive, inoder_recursive, postorder_recursive: test
  # print(bst.preorder_recursive())
  # print(bst.inorder_recursive())
  # print(bst.postorder_recursive())

  # generate_from_inorder_preorder: test
  # bst_generated = BinarySearchTree()
  # in_order, pre_order = bst.inorder_recursive(), bst.preorder_recursive()
  # bst_generated.generate_from_inorder_preorder(in_order, pre_order)

  # generate_from_inorder_postorder: test
  # bst_generated = BinarySearchTree()
  # in_order, post_order = bst.inorder_recursive(), bst.postorder_recursive()
  # bst_generated.generate_from_inorder_postorder(in_order, post_order)

  # preorder_iterative, inorder_iterative, postorder_iterative: test
  # print(bst.preorder_iterative())
  # print(bst.inorder_iterative())
  print(bst.postorder_iterative())

  # print(bst.level_order())

  # preorder_recursive, inorder_iterative_generator, postorder_recursive: test
  # for x in bst.preorder_iterative_generator(): print(x, end=''),
  # for x in bst.inorder_iterative_generator(): print(x, end=''),

  # leaf_node_generator_yield: test
  # result = []
  # for leaf in bst.leaf_node_generator_yield(bst.root):
  #   result.append(leaf)
  # print(result)

  # tree_branches_generator_yield: test
  # result = []
  # stack = []
  # for branch in bst.tree_branches_generator_yield(bst.root, stack):
  #   result.append(branch)
  # print(result)

