# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        end = head
        p = head
        for i in range(n):
            end = end.next
        if end == None:
            return head.next
        while end.next:
            end = end.next
            p = p.next
        s = p.next
        p.next = s.next
        s.next = None
        return head

