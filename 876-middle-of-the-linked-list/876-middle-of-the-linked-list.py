# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        if not head:
            return 
        else:
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
                
            middleindex = len(lst) // 2
            sliced = lst[middleindex:]
            
            newHead = ListNode()
            pointer = newHead
            for i in sliced:
                pointer.next = ListNode(i)
                pointer = pointer.next
            return newHead.next
