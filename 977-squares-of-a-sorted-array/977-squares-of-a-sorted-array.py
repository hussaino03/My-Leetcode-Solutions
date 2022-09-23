class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for i in range(len(nums)):
            s = nums[i]**2
            n.append(s)
            
        n.sort()
        return n
            