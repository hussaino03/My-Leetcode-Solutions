class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        if target not in nums:
            return [-1,-1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
                
        return [l[0], l[-1]]
                
                
                
                
    