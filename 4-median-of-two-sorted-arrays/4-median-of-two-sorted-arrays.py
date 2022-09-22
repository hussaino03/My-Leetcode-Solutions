class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # first merge the two arrays
        merged_arr = nums1 + nums2
        merged_arr.sort()
        
        if len(merged_arr) % 2 != 0:
            midd_index = len(merged_arr) // 2
            return merged_arr[midd_index]
        else:
            mid = len(merged_arr) // 2
            point = merged_arr[mid]
            beside = mid - 1
            beside_point = merged_arr[beside]
            return (point + beside_point) / 2
