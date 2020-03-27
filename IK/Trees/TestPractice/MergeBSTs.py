#!/bin/python

import os
import sys

sys.setrecursionlimit(101000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
  curr = root
  stack = []
  result = []
  while stack or curr:
    while curr:
      stack.append(curr)
      curr = curr.left
    curr = stack.pop()
    result.append(curr.key)
    curr = curr.right
  return result


def mergesorted(a, b):
  result = []
  i, j = 0, 0
  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      result.append(a[i])
      i += 1
    else:
      result.append(b[j])
      j += 1
  while i < len(a):
    result.append(a[i])
    i += 1
  while j < len(b):
    result.append(b[j])
    j += 1
  return result


def sortedarraytobst(nums):
  def helper(nums, start, end):
    if start > end: return None
    mid = start + ((end-start)//2)
    root = Node(nums[mid])
    root.left = helper(nums, start, mid-1)
    root.right = helper(nums, mid+1, end)
    return root

  if not nums: return None
  return helper(nums, 0, len(nums)-1)


# Complete this function and return root of the BST
def mergeTwoBSTs(root1, root2):
  ioroot1 = inorder(root1)
  ioroot2 = inorder(root2)
  merged = mergesorted(ioroot1,ioroot2)
  root = sortedarraytobst(merged)
  return root


def buildTree(idx, key, tree):
  root = Node(key[idx])

  if tree[idx][0] != -1:
    root.left = buildTree(tree[idx][0], key, tree)
  if tree[idx][1] != -1:
    root.right = buildTree(tree[idx][1], key, tree)
  return root


class Height:
  def __init__(self):
    self.height = 0


def isBalanced(temp, height):
  if temp is None:
    return True

  lh = Height()
  rh = Height()

  l = isBalanced(temp.left, lh)
  r = isBalanced(temp.right, rh)

  height.height = max(lh.height, rh.height) + 1

  if abs(lh.height - rh.height) <= 1 and l and r:
    return True
  return False


def inOrderTraversal(temp, f):
  if temp is None:
    return
  inOrderTraversal(temp.left, f)
  f.write(str(temp.key) + '\n')
  inOrderTraversal(temp.right, f)


if __name__ == "__main__":
  f = sys.stdout

  N1 = int(input())

  parent1 = []
  for _ in range(N1):
    operations_item = int(input())
    parent1.append(operations_item)

  child1 = []
  for _ in range(N1):
    operations_item = int(input())
    child1.append(operations_item)

  key1 = []
  for _ in range(N1):
    operations_item = int(input())
    key1.append(operations_item)

  N2 = int(input())

  parent2 = []
  for _ in range(N2):
    operations_item = int(input())
    parent2.append(operations_item)

  child2 = []
  for _ in range(N2):
    operations_item = int(input())
    child2.append(operations_item)

  key2 = []
  for _ in range(N2):
    operations_item = int(input())
    key2.append(operations_item)

  tree1 = []
  tree2 = []

  for i in range(N1):
    tree1.append([-1, -1])

  for i in range(N2):
    tree2.append([-1, -1])

  r1 = -1
  for i in range(N1):
    if parent1[i] == -1:
      r1 = i
    else:
      if child1[i] == 0:
        tree1[parent1[i]][0] = i
      elif child1[i] == 1:
        tree1[parent1[i]][1] = i

  r2 = -1
  for i in range(N2):
    if parent2[i] == -1:
      r2 = i
    else:
      if child2[i] == 0:
        tree2[parent2[i]][0] = i
      elif child2[i] == 1:
        tree2[parent2[i]][1] = i

  root1 = buildTree(r1, key1, tree1)
  root2 = buildTree(r2, key2, tree2)

  root = mergeTwoBSTs(root1, root2)
  height = Height()

  if isBalanced(root, height):
    inOrderTraversal(root, f)
  else:
    f.write('Returned tree is not height balanced\n')

  f.close()