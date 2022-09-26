# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        if not head:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
            
        mid = len(lst) // 2
        lst.pop(mid)
        
        newH = ListNode()
        pointer = newH
        for i in lst:
            pointer.next = ListNode(i)
            pointer = pointer.next
            
        return newH.next