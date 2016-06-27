# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        if m == 1:
            header = ListNode(0)
            header.next = head
        else:
            header = head
            for i in range(m-2):
                header = header.next
        s = header.next
        first = s
        for i in range(n-m+1):
            r = s.next
            s.next = header.next
            header.next = s
            s = r
        first.next = r
        if m == 1 :
            return header.next
        else:
            return head

