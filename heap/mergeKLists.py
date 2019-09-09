'''
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
23. Merge k Sorted Lists
Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    head = tail = ListNode(-1)
    while l1 and l2:
      if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return head.next

  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    ret = ListNode(-sys.maxint - 1)
    for l in lists:
      ret = self.mergeTwoLists(ret, l)
    return ret.next