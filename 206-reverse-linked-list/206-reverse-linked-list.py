# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr, nex = head, head.next
        curr.next = None
        while nex is not None:
            tmp = nex
            nex = nex.next
            tmp.next = curr
            curr = tmp
        return curr
