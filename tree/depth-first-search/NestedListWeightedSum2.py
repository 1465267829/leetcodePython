'''
364. Nested List Weight Sum II
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
#        Otherwise initializes a single integer equal to value.
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

class Solution(object):
  def depthSumInverse(self, nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    if not len(nestedList): return 0

    queue = nestedList
    depth_sum_list = []
    depth_sum_list.append(0)
    while queue:
      levelSum = 0
      for _ in range(len(queue)):
        current = queue.pop(0)
        if isinstance(current, int):
          levelSum += current
        else:
          for element in current:
            queue.append(element)
      depth_sum_list.append(levelSum)

    depthInverseSum = 0
    for weight, depthSum in enumerate(reversed(depth_sum_list)):
      depthInverseSum += (weight + 1) * depthSum
    return depthInverseSum

if __name__ == '__main__':
  # nested_list = [[1,1],0,[1,[2]]]
  nested_list = [[1,1],2,[1,1]]
  # nested_list = [[[[[]]]],[[[[[[[[[[[[[[1]]]]],-5]]]]]]]]],[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[45]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

  s = Solution()
  print(s.depthSumInverse(nested_list))