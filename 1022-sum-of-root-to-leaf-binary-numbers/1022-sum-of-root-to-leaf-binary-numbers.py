# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.binary(root, 0)
    
    def binary(self, node: TreeNode, val: int):
        if node is None:
            return 0

        val = val * 2 + node.val
        
        if not node.left and not node.right:
            return val
        
        return self.binary(node.left, val) + self.binary(node.right, val)
