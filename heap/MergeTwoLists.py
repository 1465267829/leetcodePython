'''
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists
Easy

2578

373

Favorite

Share
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(-1)
    tail = head
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

def sllify(list):
  head = ListNode(-1)
  tail = head
  for i in list:
    tail.next = ListNode(i)
    tail = tail.next
  return head.next

if __name__ == '__main__':
  a1 = [1, 2, 4]
  a2 = [1, 3, 4]
  l1 = sllify(a1)
  l2 = sllify(a2)
  sol = Solution()
  l3 = sol.mergeTwoLists(l1, l2)
  pass
