import sys

sys.setrecursionlimit(101000)

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node == None:
        return None
    preorder(node.left)
    preorder(node.right)


# class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

def helper(current, a, b, ans):
  if not current:
    return False
  if_in_left_subtree = helper(current.left, a, b, ans)
  if_in_right_subtree = helper(current.right, a, b, ans)
  if_current = True if current.data == a.data or current.data == b.data else False
  if current.data == a.data and current.data == b.data:
    ans.append(current)
    return True
  if if_in_left_subtree and if_in_right_subtree:
    ans.append(current)
    return True
  if if_in_left_subtree and if_current:
    ans.append(current)
    return True
  if if_in_right_subtree and if_current:
    ans.append(current)
    return True
  if if_in_left_subtree or if_in_right_subtree or if_current:
    return True
  return False


def lca(root, a, b):
  # Write your code here
  ans = []
  helper(root, a, b, ans)
  ret = ans[0].data if ans else None
  return ret

numbers = [int(n) for n in input().split()]
n=numbers[0]
a=numbers[1]
b=numbers[2]

i=0
xx=[]
while i<=n:
    xx.insert(i,Node(i,None,None))
    i+=1;
i=1
while i<n:
    num = [int(n) for n in input().split()]
    st=num[0]
    en=num[1]
    if xx[st].left==None:
        xx[st].left=xx[en]
    else:
        xx[st].right=xx[en]
    i+=1

print(lca(xx[1], xx[a], xx[b]))