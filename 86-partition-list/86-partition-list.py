# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lst, left, right = [], [], []
        if not head:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
            
        for i in lst:
            if i < x:
                left.append(i)
            else:
                right.append(i)
                
        res = left + right
        newH = ListNode()
        pointer = newH
        for i in res:
            pointer.next = ListNode(i)
            pointer = pointer.next
            
        return newH.next