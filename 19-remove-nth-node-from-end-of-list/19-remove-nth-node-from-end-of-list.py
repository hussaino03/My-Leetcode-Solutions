# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst, temp, res = [], [], []
        if head is None:
            return 
        else:
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
                
            for v in lst:
              temp = [v] + temp
            
            i = 0
            while i <= len(temp):
                if i == n-1:
                    temp.pop(i)
                    
                i += 1
                    
            for x in temp:
              res = [x] + res
            
            newHead = ListNode()
            pointer = newHead
            for i in res:
                pointer.next = ListNode(i)
                pointer = pointer.next
            return newHead.next
            
                            
                