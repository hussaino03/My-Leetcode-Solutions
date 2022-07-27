# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
                return False 
            
        else:
            r = self.check(left.left, right.right)
            if r:
                return self.check(left.right, right.left)
        