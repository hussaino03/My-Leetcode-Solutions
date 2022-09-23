class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for num in nums1:
            if num in nums2:
                lst.append(num)
                    
        return set(lst)