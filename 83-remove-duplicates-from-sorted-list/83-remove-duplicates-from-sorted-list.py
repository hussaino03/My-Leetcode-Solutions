# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            curr = head
            while curr.next is not None:
                if curr.val != curr.next.val:
                    curr = curr.next
                else:
                    curr.next = curr.next.next
                    
            return head
            
