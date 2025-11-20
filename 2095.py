# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        p=dummy
        s=head
        f=head
        while f and f.next:
            p=s
            s=s.next
            f=f.next.next
        p.next=s.next
        return dummy.next
