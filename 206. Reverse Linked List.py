# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        while head:
            s = head.next
            head.next = header.next
            header.next = head
            head = s
        return header.next