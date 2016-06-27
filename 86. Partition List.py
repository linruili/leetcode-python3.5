# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        less = ListNode(0)
        less.next = head
        dummy = less
        cur = head
        while cur and cur.val<x:
            cur = cur.next
            less = less.next
        cur = less.next
        pre = less
        while  cur:
            if cur.val>=x:
                pre , cur = cur ,cur.next
            else:
                pre.next = cur.next
                cur.next = less.next
                less.next = cur
                less = less.next
                cur = pre.next
        return dummy.next

