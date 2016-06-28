# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        fast , slow = head.next , head
        while fast and slow :
            if fast==slow:
                return True
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            if fast == slow:
                return True
            fast = fast.next
        return False

