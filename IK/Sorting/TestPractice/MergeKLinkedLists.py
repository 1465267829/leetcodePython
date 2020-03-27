"""

https://leetcode.com/problems/merge-k-sorted-lists/

23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue
import sys


class Solution:
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = PriorityQueue()
    dummy = ListNode(- sys.maxsize - 1)
    last = dummy
    for index, head in enumerate(lists):
      if head: heap.put((head.val, index, head))

    while not heap.empty():
      _, index, smallest_node = heap.get()
      if smallest_node.next: heap.put((smallest_node.next.val, index, smallest_node.next))
      last.next = smallest_node
      last = last.next
    return dummy.next



