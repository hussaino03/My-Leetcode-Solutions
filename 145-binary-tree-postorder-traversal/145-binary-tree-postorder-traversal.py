# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        
        else:
            l = self.postorderTraversal(root.left)
            r = self.postorderTraversal(root.right)
            return l + r + [root.val]