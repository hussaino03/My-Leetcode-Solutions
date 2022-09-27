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
        
        res = self.msort2(linkedList)
        pointer = newHead = ListNode()
        for i in res:
            pointer.next = ListNode(i)
            pointer = pointer.next
        return newHead.next
    
    def msort2(self, x):
        if len(x) < 2:
            return x
        result = []          
        mid = int(len(x) / 2)
        y = self.msort2(x[:mid])
        z = self.msort2(x[mid:])
        while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        result += y
        result += z
        return result
                    