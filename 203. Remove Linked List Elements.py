# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head.val == val:
            head = head.next
            if head == None:
                return None
        p , q = head , head.next
        while q:
            if q.val == val:
                p.next = q.next
                q.next = None
                q = p.next
            else:
                q = q.next
                p = p.next
        return head
