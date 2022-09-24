# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        if not head:
            return False
        else:
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
                
            if lst == lst[::-1]:
                return True
            else:
                return False