# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None or head.next.next==None:
            return 
        p ,head1, head2 = head , head , head
        while p:
            p = p.next
            if p:
                p = p.next
            head2 = head2.next#head1 tail's next
        dummy = ListNode(0)
        while head2:
            s = head2
            head2 = head2.next
            s.next = dummy.next
            dummy.next = s
        head2 = dummy.next
        while head2:
            s = head2
            head2 = head2.next
            s.next = head1.next
            head1.next = s
            head1 = s.next
        head1.next = None

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s = Solution()
    s.reorderList(head)
    while head:
        print(head.val)
        head = head.next




