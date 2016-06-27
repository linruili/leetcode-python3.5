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
        while head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            if head.next:
                head = head.next
            else:
                return None
        pre , cur = head , head.next
        while cur:
            tag = 0
            while cur.next and cur.val==cur.next.val:
                cur = cur.next
                tag =1
            if tag==1:
                cur = cur.next
                pre.next = cur
            else:
                pre , cur = pre.next , cur.next
        return head

