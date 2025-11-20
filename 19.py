# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        s=dummy
        f=dummy
        for _ in range(n):
            if f.next is None:
                return head
            f=f.next
        while f.next:
            s=s.next
            f=f.next
        n=s.next
        s.next=n.next
        return dummy.nex
