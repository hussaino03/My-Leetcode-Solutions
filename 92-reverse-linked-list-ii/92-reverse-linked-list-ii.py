# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst, lst1 = [], []
        if not head:
            return
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        
        a=left
        b=right
        a=a-1
        lst1=lst[a:b]
        lst1.reverse()
        lst[a:b]=lst1

        dummyhead=ListNode()
        jus=dummyhead
        for i in lst:
            node=ListNode(i)
            jus.next=node
            jus=jus.next

        return dummyhead.next
        
            