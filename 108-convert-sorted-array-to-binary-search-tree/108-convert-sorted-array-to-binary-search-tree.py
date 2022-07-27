# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        mid = len(nums) // 2
        curr = TreeNode()
        curr.val = nums[mid]
        curr.left = self.sortedArrayToBST(nums[:mid])
        curr.right = self.sortedArrayToBST(nums[mid + 1 :])
        return curr
        
        