'''
339. Nested List Weight Sum
https://leetcode.com/problems/nested-list-weight-sum/
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherxwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class SolutiondepthSum(object):

  # Acceptable Leetcode
  def depthSum(self, nestedList):
    def helper(nestedList, depth):
      sum = 0
      for element in nestedList:
        if isinstance(element, int):
          sum += depth * element
        else:
          sum += helper(element, depth + 1)
      return sum
    if not nestedList: return 0
    return helper(nestedList, 1)

  def depthSumIterative(self, nestedList):
    if len(nestedList) == 0: return 0
    queue = nestedList
    depthSum = 0
    depth = 0
    while queue:
      depth += 1
      levelSum = 0
      for _ in range(len(queue)):
        current = queue.pop(0)
        if isinstance(current, int):
          levelSum += current
        else:
          for element in current:
            queue.append(element)
      depthSum += (depth * levelSum)
    return depthSum

if __name__ == '__main__':
  nested_list = [[1,1],2,[1,[2]]]
  s = SolutiondepthSum()
  print(s.depthSum(nested_list))
  print(s.depthSumIterative(nested_list))