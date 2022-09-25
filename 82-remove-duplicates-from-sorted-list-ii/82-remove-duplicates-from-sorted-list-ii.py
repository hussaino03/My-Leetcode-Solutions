# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        if head is None:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        
        for x in set(lst):
            if lst.count(x) > 1:
                while x in lst:
                    lst.remove(x)
        newH = ListNode()
        newcurr = newH
        for i in lst:
            newcurr.next = ListNode(i)
            newcurr = newcurr.next
        return newH.next
    
    