# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst, odd, even = [], [], []
        if not head:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
            
        for i in range(len(lst)):
            if i % 2 == 0:
                even.append(lst[i])
            else:
                odd.append(lst[i])
                
        res = even + odd
            
        newH = ListNode()
        pointer = newH
        for i in res:
            pointer.next = ListNode(i)
            pointer = pointer.next
            
        return newH.next
                
        