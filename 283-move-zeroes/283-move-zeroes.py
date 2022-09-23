class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        zero = 0
        while a < len(nums):
            if nums[a] != 0:
                nums[a], nums[zero] = nums[zero], nums[a]
                zero += 1
            a += 1
                
        return nums
