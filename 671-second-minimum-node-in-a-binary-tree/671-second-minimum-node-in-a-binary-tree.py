# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.val = []
        
        def getValue(root):
            if root is None:
                return 0
            self.val.append(root.val)
            getValue(root.left)
            getValue(root.right)
        
        getValue(root)
        val = sorted(set(self.val))
        return val[1] if len(val)>1 else -1
    


                
            