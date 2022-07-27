# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            if root.left is None or root.right is None:
                return max(l, r) +1
            else:
                return min(l, r) + 1