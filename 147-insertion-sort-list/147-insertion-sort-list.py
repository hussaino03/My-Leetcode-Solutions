# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        else:
            lst = []
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
            
            lst.sort()
            newHead = ListNode()
            pointer = newHead
            for i in lst:
                pointer.next = ListNode(i)
                pointer = pointer.next
                
            return newHead.next
