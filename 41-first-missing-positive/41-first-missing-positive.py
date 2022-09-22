class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums.sort()
        if ans in nums:
            for i in range(len(nums)):
                a = nums[i]
                if a == ans:
                    ans = ans+1        
        return ans