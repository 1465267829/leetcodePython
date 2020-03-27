import sys
from collections import deque

sys.setrecursionlimit(100000 + 1000)


class TreeNode():
  def __init__(self, val=None, left_ptr=None, right_ptr=None):
    self.val = val
    self.left_ptr = left_ptr
    self.right_ptr = right_ptr


class BinaryTree():
  class Edge():
    def __init__(self, parentNodeIndex=None, childNodeIndex=None, leftRightFlag=None):
      self.BinaryTree = BinaryTree
      self.parentNodeIndex = parentNodeIndex
      self.childNodeIndex = childNodeIndex
      self.leftRightFlag = leftRightFlag

  def __init__(self):
    self.root = None;
    self.noOfNodes = 0
    self.noOfEdges = 0
    self.rootIndex = -1
    self.nodeValues = []
    self.edges = []

  def readRawValues(self):
    self.noOfNodes = int(input())
    if self.noOfNodes > 0:
      nodeValueString = input().split(' ')
      for val in nodeValueString:
        self.nodeValues.append(int(val))

    self.rootIndex = int(input())
    self.noOfEdges = int(input())
    for i in range(self.noOfEdges):
      edgeInput = input().split(' ')
      self.edges.append(self.Edge(int(edgeInput[0]), int(edgeInput[1]), edgeInput[2]))

  def buildFormRawValues(self):
    if self.noOfNodes == 0:
      root = None
      return
    nodes = []
    for i in range(self.noOfNodes):
      nodes.append(TreeNode(self.nodeValues[i]))

    for i in range(self.noOfEdges):
      if self.edges[i].leftRightFlag == "L":
        nodes[self.edges[i].parentNodeIndex].left_ptr = nodes[self.edges[i].childNodeIndex]
      else:
        nodes[self.edges[i].parentNodeIndex].right_ptr = nodes[self.edges[i].childNodeIndex]

    self.root = nodes[self.rootIndex]


def readBinaryTree():
  inputBinaryTree = BinaryTree()
  inputBinaryTree.readRawValues()
  inputBinaryTree.buildFormRawValues()
  return inputBinaryTree.root


def printArray(result):
  if result == None:
    print()
    return
  for i in range(0, len(result)):
    if i > 0:
      print(end=' ')
    print(result[i], end='')
  print()


def postorderTraversal(root):
  if not root:
    return []
  stack, current, result = [], root, []
  while current or stack:
    while current:
      result.append(str(current.val))
      stack.append(current)
      current = current.right_ptr
    current = stack.pop()
    current = current.left_ptr
  result = list(reversed(result))
  return result

def main():
  root = readBinaryTree()
  result = postorderTraversal(root)
  printArray(result)

main()