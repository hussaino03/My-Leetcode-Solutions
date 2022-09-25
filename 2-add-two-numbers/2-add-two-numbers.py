# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l, s = [], []
        if not l1 or not l2:
            return
        else:
            while l1 is not None:
                l.append(l1.val)
                l1 = l1.next
            while l2 is not None:
                s.append(l2.val)
                l2 = l2.next
                
        for i in range(len(l) // 2):
            l[i], l[-1 - i] = l[-1 - i], l[i]
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]
        
        a = int("".join(str(i) for i in l))
        b = int("".join(str(i) for i in s))
        
        tmp = [a + b]
        
        res = list(map(int, list(str(tmp[0]))))
        res.reverse()
        
        newH = ListNode()
        pointer = newH
        for i in res:
            pointer.next = ListNode(i)
            pointer = pointer.next
            
        return newH.next
        
        