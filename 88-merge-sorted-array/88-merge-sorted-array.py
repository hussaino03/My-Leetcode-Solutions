class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)==0 or len(nums2)==0:
            nums1 = nums1+nums2
        
        for i in range(len(nums1)-m):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()