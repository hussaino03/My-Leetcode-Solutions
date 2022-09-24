# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        if head is None:
            return 
        else:
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
                
            lst.reverse()
            
            i = 0
            while i <= len(lst):
                if i == n-1:
                    lst.pop(i)
                    
                i += 1
                    
            lst.reverse()
            newHead = ListNode()
            pointer = newHead
            for i in lst:
                pointer.next = ListNode(i)
                pointer = pointer.next
            return newHead.next
            
                            
                