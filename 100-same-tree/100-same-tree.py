# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        
        elif p is None or q is None:
            return False
        
        elif p.val != q.val:
            return False
        
        elif (p.right is None and q.right is None) and (p.left is None and q.left is None):
            return p.val == q.val
        
        else:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        