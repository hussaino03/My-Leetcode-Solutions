# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        linkedList = []
        current = head
        while current:
            linkedList.append(current.val)
            current = current.next
            
        linkedList.sort()
        
        pointer = newHead = ListNode()
        for i in linkedList:
            pointer.next = ListNode(i)
            pointer = pointer.next
        return newHead.next
                    