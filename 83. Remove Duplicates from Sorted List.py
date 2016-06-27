# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        pre , cur = head , head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            else:
                pre , cur = pre.next , pre.next.next
        return head

