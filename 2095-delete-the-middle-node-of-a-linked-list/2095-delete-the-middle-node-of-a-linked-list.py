# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        counter = 0
        if not head:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            counter += 1
            curr = curr.next
            
        mid = counter // 2
        del lst[mid]
        
        newH = ListNode()
        pointer = newH
        for i in lst:
            pointer.next = ListNode(i)
            pointer = pointer.next
            
        return newH.next