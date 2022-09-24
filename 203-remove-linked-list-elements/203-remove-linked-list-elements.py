# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        lst = []
        if head is None:
            return None
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
            
        
        while val in lst:
            lst.remove(val)
                
                
        newh = ListNode()
        newcurr = newh
        for i in lst:
            newcurr.next = ListNode(i)
            newcurr = newcurr.next
        return newh.next